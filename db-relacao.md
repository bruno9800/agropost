- USERS

  -> user django contrib

  - username
  - email
  - password

- following
- friends
- bio
- date_of_birth
- updated_at
- created_at
- image

- MARCA (FAZER)

  - name
  - products -> relação com PRODUCT

- PRODUCT

  - name
  - brand
  - picture
  - product_type
  - posts -> Relação com POST

- POST

  - title
  - content
  - rate
  - published_at
  - updated_at
  - product -> relação com PRODUCT
  - author -> relação com User
  - upgrade -> relação com User
  - downgrade -> relação com User

- COMMENT

  - post -> Relação com POST
  - author -> Relação com User
  - content
  - created_at
  - likes -> relação com User
