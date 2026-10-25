package ir.darookhaneh.stock.core.data.pharmacy

import ir.darookhaneh.stock.core.database.entity.BatchEntity
import ir.darookhaneh.stock.core.database.entity.DrugEntity
import ir.darookhaneh.stock.core.database.entity.DrugSummaryRow
import ir.darookhaneh.stock.core.database.entity.InventoryEventEntity
import ir.darookhaneh.stock.core.model.pharmacy.Batch
import ir.darookhaneh.stock.core.model.pharmacy.Drug
import ir.darookhaneh.stock.core.model.pharmacy.DrugSummary
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEvent
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType

/** تبدیل بین مدل دامنه و ردیف Room. هیچ قاعده‌ای اینجا پیاده نمی‌شود. */

fun DrugEntity.toDomain(): Drug = Drug(
    id = id,
    name = name,
    genericName = genericName,
    strength = strength,
    dosageForm = dosageForm,
    gtin = gtin,
    irc = irc,
    createdAt = createdAt,
    updatedAt = updatedAt,
)

fun BatchEntity.toDomain(): Batch = Batch(
    id = id,
    drugId = drugId,
    batchNumber = batchNumber,
    expiryDate = expiryDate,
    quantity = quantity,
    location = location,
    createdAt = createdAt,
    updatedAt = updatedAt,
)

fun InventoryEventEntity.toDomain(): InventoryEvent = InventoryEvent(
    id = id,
    batchId = batchId,
    type = InventoryEventType.fromStorage(type),
    quantityDelta = quantityDelta,
    note = note,
    createdAt = createdAt,
)

fun InventoryEventType.toStorage(): String = name

fun DrugSummaryRow.toDomain(lowStockThreshold: Int): DrugSummary = DrugSummary(
    id = id,
    name = name,
    genericName = genericName,
    strength = strength,
    dosageForm = dosageForm,
    gtin = gtin,
    irc = irc,
    totalQuantity = totalQuantity,
    batchCount = batchCount,
    nearestExpiry = nearestExpiry,
    isLowStock = totalQuantity <= lowStockThreshold,
)
