import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                  Column('employee_id', Integer, ForeignKey('employee.id'))
)

def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name

class MenuItem(Model):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    link = Column(String(150), nullable=False)
    menu_category_id = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    menu_category = relationship("MenuCategory")

class MenuCategory(Model):
    __tablename__ = 'menu_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('news_category.id'), nullable=False)
    newsCat = relationship("NewsCategory")

class NewsCategory(Model):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
 
class ProductType(Model):
    __tablename__ = 'product_type'
    id = Column(Integer, primary_key=True)
    type = Column(String(100), nullable=False)
    
    
class Supplier(Model):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    address = Column(String(200), nullable=False)

class Product(Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    shelf_date = Column(Date, default=datetime.date.today(), nullable=True)
    stock = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    supplier_id = Column(Integer, ForeignKey('supplier.id'), nullable=False)
    supplier = relationship("Supplier")
    product_type_id = Column(Integer, ForeignKey('product_type.id'), nullable=False)
    product_type = relationship("ProductType")

    def __repr__(self):
        return self.name
    
class Invoice(Model):
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    product_name = Column(String(100), nullable=False, unique=True)
    purchase_time = Column(Date, default=datetime.date.today(), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    customer_name = Column(String(100), nullable=False)
    store_address = Column(String(200), nullable=False, unique=True)
    total_amount = Column(Integer, nullable=False)
        
class Customer(Model):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    address = Column(String(200), nullable=True)
    
class ShoppingCart(Model):
    __tablename__ = 'shopping_cart'
    id = Column(Integer, primary_key=True)
    product_name = Column(String(100), nullable=False, unique=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(String(100), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    customer_name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    created_time = Column(Date, default=datetime.date.today(), nullable=False)
    
class StoreInfo(Model):
    __tablename__ = 'store_info'
    id = Column(Integer, primary_key=True)
    address = Column(String(200), nullable=False, unique=True)
    telephone = Column(Integer, nullable=False, unique=True)
    
class Coupon(Model):
    __tablename__ = 'coupon'
    id = Column(Integer, primary_key=True)
    expired_time = Column(Date, default=datetime.date.today(), nullable=False)
    amount = Column(Integer, nullable=False)

class JoinUs(Model):
    __tablename__ = 'join_us'
    id = Column(Integer, primary_key=True)
    post_time = Column(Date, default=datetime.date.today(), nullable=False)
    job_title = Column(String(100), nullable=False, unique=True)
    address = Column(String(200), nullable=False)