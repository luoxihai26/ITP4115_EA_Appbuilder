from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import MenuCategory, News, NewsCategory, StoreInfo, Product, JoinUs, Supplier, ProductType, Customer, ShoppingCart, Coupon, Invoice
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']

class NewsPageView(BaseView):
    default_view = 'local_news'

    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/global_news/')
    def global_news(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)

class StoreInfoView(ModelView):
    datamodel = SQLAInterface(StoreInfo)
    list_columns = ['id', 'address', 'telephone']
  
class StoreInfoPageView(BaseView):
    default_view = 'store_info'
    
    @expose('/store_info/')
    def store_info(self):
        param1 = 'Store Information'
        self.update_redirect()
        return self.render_template('store_info.html', param1=param1)
        
class ProductView(ModelView):
    datamodel = SQLAInterface(Product)
    list_columns = ['id', 'name', 'shelf_date', 'stock', 'price', 'product_type', 'supplier']
    
class ProductTypeView(ModelView):
    datamodel = SQLAInterface(ProductType)
    list_columns = ['id', 'type']
    #related_views = [ProductView]
    
class SupplierView(ModelView):
    datamodel = SQLAInterface(Supplier)
    list_columns = ['id', 'name', 'address', 'product_id', 'product_name', 'products']
    #related_views = [ProductView]


class ShoppingCartView(ModelView):
    datamodel = SQLAInterface(ShoppingCart)
    list_columns = ['id', 'product_name', 'quantity', 'customer_name', 'price', 'created_time']
    
class CouponView(ModelView):
    datamodel = SQLAInterface(Coupon)
    list_columns = ['id', 'expired_date', 'amount']

class InvoiceView(ModelView):
    datamodel = SQLAInterface(Invoice)
    list_columns = ['id', 'product_name', 'purchase_time', 'customer_name', 'store_address', 'total_amount']

class CustomerView(ModelView):
    datamodel = SQLAInterface(Customer)
    list_columns = ['id', 'full_name', 'username', 'password', 'email', 'address']

class JoinUsView(ModelView):
    datamodel = SQLAInterface(JoinUs)
    list_columns = ['id', 'post_time', 'job_title', 'address']

class JoinUsPageView(BaseView):
    default_view = 'join_us'
    
    @expose('/join_us/')
    def join_us(self):
        param1 = 'Join Us'
        self.update_redirect()
        return self.render_template('join_us.html', param1=param1)


db.create_all()

""" Page View """
appbuilder.add_view(StoreInfoPageView, 'Store Information', category="Store")
appbuilder.add_view(JoinUsPageView, 'JoinUs', category="Join Us")

""" Custom Views """
appbuilder.add_view(StoreInfoView, "StoreInfo", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(ProductView, "Product", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(JoinUsView, "JoinUs", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(SupplierView, "Supplier", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(ProductTypeView, "ProductType", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(ShoppingCartView, "ShoppingCart", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(CouponView, "Coupon", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(InvoiceView, "Invoice", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(CustomerView, "Customer", icon="fa-folder-open-o", category="Admin")