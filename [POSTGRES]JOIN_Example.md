
```
SELECT products.product_id,
  products.name,
  products.manufacturing_cost,
  categories.name,
  categires.market
FROM manufacturing.products JOIN manufacturing.categories
ON products.category_id = categories.category_id;

```
