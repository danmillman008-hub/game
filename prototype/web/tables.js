"use strict";
const NE = require(require("path").join(__dirname, "neon_alley.js"));
process.stdout.write(JSON.stringify({
  z_table: NE.Z_TABLE,
  body_box_table: NE.BODY_BOX_TABLE,
}) + "\n");
