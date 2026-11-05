#!/usr/bin/env python3
"""Dependency-free validator for MIMO_INFORMATION_FORM.json packages.

Supports the JSON-Schema subset used by the form: $ref, type, required,
properties, items, enum, const, pattern, minimum, minItems, additionalProperties.
Usage: python3 app/tools/validate_content.py <package.json> [...]
"""
from __future__ import annotations
import json, os, re, sys

FORM = os.path.join(os.path.dirname(__file__), '..', 'content', 'MIMO_INFORMATION_FORM.json')


def resolve(schema, root):
    if '$ref' in schema:
        ref = schema['$ref']
        assert ref.startswith('#/'), f'unsupported ref {ref}'
        cur = root
        for part in ref[2:].split('/'):
            cur = cur[part]
        return cur
    return schema


def validate(value, schema, root, path, errors):
    s = resolve(schema, root)
    t = s.get('type')
    if t == 'object':
        if not isinstance(value, dict):
            errors.append(f'{path}: expected object, got {type(value).__name__}')
            return
        for k in s.get('required', []):
            if k not in value:
                errors.append(f'{path}: missing required field "{k}"')
        props = s.get('properties', {})
        if s.get('additionalProperties') is False:
            for k in value:
                if k not in props:
                    errors.append(f'{path}: unexpected field "{k}"')
        for k, v in value.items():
            if k in props:
                validate(v, props[k], root, f'{path}.{k}', errors)
    elif t == 'array':
        if not isinstance(value, list):
            errors.append(f'{path}: expected array')
            return
        if 'minItems' in s and len(value) < s['minItems']:
            errors.append(f'{path}: expected >= {s["minItems"]} items, got {len(value)}')
        if 'items' in s:
            for i, v in enumerate(value):
                validate(v, s['items'], root, f'{path}[{i}]', errors)
    elif t == 'string':
        if not isinstance(value, str):
            errors.append(f'{path}: expected string')
        elif 'pattern' in s and not re.search(s['pattern'], value):
            errors.append(f'{path}: does not match {s["pattern"]}')
    elif t == 'integer':
        if not isinstance(value, int) or isinstance(value, bool):
            errors.append(f'{path}: expected integer')
        elif 'minimum' in s and value < s['minimum']:
            errors.append(f'{path}: below minimum {s["minimum"]}')
    elif t == 'number':
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            errors.append(f'{path}: expected number')
        elif 'minimum' in s and value < s['minimum']:
            errors.append(f'{path}: below minimum')
        elif 'maximum' in s and value > s['maximum']:
            errors.append(f'{path}: above maximum')
    elif t == 'boolean':
        if not isinstance(value, bool):
            errors.append(f'{path}: expected boolean')
    if 'const' in s and value != s['const']:
        errors.append(f'{path}: must equal {s["const"]!r}')
    if 'enum' in s and value not in s['enum']:
        errors.append(f'{path}: {value!r} not in {s["enum"]}')


def main(argv):
    root = json.load(open(FORM, encoding='utf-8'))
    targets = argv[1:] or [os.path.join(os.path.dirname(FORM), 'CONTENT_FORM_TEMPLATE.json')]
    bad = 0
    for p in targets:
        try:
            data = json.load(open(p, encoding='utf-8'))
        except Exception as e:
            print(f'FAIL {p}: {e}')
            bad += 1
            continue
        errors = []
        validate(data, root, root, '$', errors)
        if errors:
            bad += 1
            print(f'FAIL {p}: {len(errors)} error(s)')
            for e in errors[:25]:
                print('   ', e)
        else:
            status = data.get('source', {}).get('contentStatus')
            print(f'PASS {p}  (tracks={len(data.get("tracks", []))}, '
                  f'questions={len(data.get("questions", []))}, '
                  f'exams={len(data.get("exams", []))}, contentStatus={status})')
    print(f'validated: {len(targets)}  passed: {len(targets)-bad}  failed: {bad}')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
