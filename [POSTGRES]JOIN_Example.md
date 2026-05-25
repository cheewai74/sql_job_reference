
```
SELECT products.product_id,
  products.name AS product_name,
  products.manufacturing_cost,
  categories.name AS product_name,
  categires.market
FROM manufacturing.products JOIN manufacturing.categories
ON products.category_id = categories.category_id;

```

```
CREATE VIEW manufacturing.products_details AS
SELECT products.product_id,
       products.name AS product_name,
       products.manufacturing_cost,
       categories.name AS category_name,
       categories.market
FROM manufacturing.products
INNER JOIN manufacturing.categories
ON products.category_id = categories.category_id;
```
