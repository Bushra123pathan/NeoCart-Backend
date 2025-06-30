
#  NeoCart - E-commerce Backend

**NeoCart** is a Django REST Framework-based backend solution for an e-commerce platform.  
It provides secure user authentication, product management, cart functionality, and order processing, all with role-based access.

---

## Functional Features

### 1. User Management

- User registration and login using **JWT authentication**
- **Three user roles**:
  - **Admin** – Manage all users, products, and orders
  - **Seller** – Add, update, and manage their own products, view orders related to their products
  - **Customer** – Browse products, manage cart, place orders
- Role-based access control across all endpoints
- API to view and update user profile

---

### 2. Product Management

- CRUD operations by **seller** or **admin**
- Product fields: `title`, `description`, `price`, `stock`, `category`, `image_url`
- Product listing with:
  -  Search by name
  -  Filter by category and price range
  -  Sorting (ordering by price or other fields)
  -  Pagination support
- Product detail API

---

### 3.  Cart Management

- Customers can:
  - Add products to cart
  - Update quantity
  - Remove items
- Only one active cart per customer
- Auto-calculation of total cart value

---

### 4.  Order Management

- Customers can place orders directly from their cart
- Order includes:
  - Unique order ID
  - Total price
  - List of ordered items
  - Order status and timestamp
- Order status lifecycle: `Placed → Shipped → Delivered`
- Sellers can view orders related to their products
- Admins can view and manage all orders

---

### 5.  Role-Based Access Control (RBAC)

- APIs protected using **custom permissions**
- Only authorized roles can perform specific actions  
  (e.g., only sellers can add products, only customers can place orders)

---

##  Non-Functional Features

| Feature              | Description |
|----------------------|-------------|
|  **Authentication**  | JWT-based access & refresh tokens using `djangorestframework-simplejwt` |
|  **Authorization**   | Role-based access using custom permission classes |
|  **Validation**      | Handled in **serializers**, not in views |
|  **Pagination**      | Applied to product listings and order history |
|  **Filtering/Search**| By name, category, price range via query parameters |
|  **Modular Structure**| Django apps: `users`, `products`, `cart`, `orders`, `common` |
|  **Database Design** | Proper relational structure using ForeignKeys |
|  **Error Handling**  | Standardized error messages and HTTP status codes |
|  **Security**        | All endpoints protected via authentication/authorization |
|  **RESTful Design**  | Follows REST principles: GET, POST, PUT, DELETE |
|  **Scalability**     | Modular, extendable codebase |
|  **Extensibility**   | Easy to add future modules |

---

##  Optional / Future Enhancements

-  Product **review and rating system**
-  **Payment** simulation (UPI, Card, COD)
-  **Wishlist** feature
-  Admin **analytics dashboard** (users, revenue, etc.)
-  **PDF invoice generation** for completed orders

---

##  Project Modules Overview

| Module     | Description                              |
|------------|------------------------------------------|
| `users`    | Registration, login, JWT auth, roles     |
| `products` | Product CRUD, search, filtering          |
| `cart`     | Cart add/update/delete by customers      |
| `orders`   | Place order, track history               |
| `common`   | (Optional) Shared logic, utils, permissions |

---

##  Getting Started

```bash
# Clone the repo
git clone https://github.com/Bushra123pathan/NeoCart-Backend.git
cd NeoCart-Backend

# Create and activate virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

---

## 🔑 Authentication Guide

###  Login Endpoint
```http
POST /api/login/
```

**Response**: Returns access and refresh tokens

**Use in Headers**:
```http
Authorization: Bearer <access_token>
```

---

##  Sample API Endpoints

| Method | Endpoint                       | Access        | Description                      |
|--------|--------------------------------|---------------|----------------------------------|
| GET    | /api/products/                 | Public        | List all products                |
| POST   | /api/products/                 | Seller/Admin  | Add new product                  |
| GET    | /api/cart/                     | Customer      | View cart                        |
| POST   | /api/cart/                     | Customer      | Add item to cart                 |
| DELETE | /api/cart/<item_id>/           | Customer      | Remove item from cart            |
| POST   | /api/orders/                   | Customer      | Place order from cart            |
| GET    | /api/orders/                   | Customer      | View order history               |

---

##  Postman Testing Tips

### 1. Login as Seller / Customer
```json
POST /api/login/
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

### 2. Use the Access Token in Headers
```http
Authorization: Bearer <your_access_token>
```

### 3. Example Product Filter Usage
```http
GET /api/products/?search=phone&category=Electronics&price_min=1000&price_max=50000&page=1
```

---

##  Superuser Setup (Admin Panel)
```bash
python manage.py createsuperuser
```

Then open:
```
http://127.0.0.1:8000/admin/
```

---

##  Future Enhancements

-  Product reviews & ratings  
-  Payment simulation (UPI, COD)  
-  Wishlist functionality  
-  Admin dashboard (orders, users, revenue)  
-  PDF invoice generation  

---

##  License

This project is licensed under the MIT License.