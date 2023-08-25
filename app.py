import json
import re
import webbrowser
from nltk.corpus import stopwords
import nltk
from  kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDTextButton
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.tooltip import MDTooltip
from kivymd.uix.button import MDIconButton
import uuid
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.relativelayout import MDRelativeLayout
import requests
from kivy.uix.image import AsyncImage
from kivy.loader import Loader
from bs4 import BeautifulSoup
from kivy.uix.button import Button
from kivymd.uix.toolbar import MDToolbar
import pickle
import pandas as pd
custom_template = """
    [color=#000000][size=20]{}[/size][/color]
"""

helpstr = '''
ScreenManager:
    BackgroundScreen:
    SecondScreen:
    ThirdScreen:
    ProductInfo:
    ReviewScreen:
<Background>:
    orientation: "vertical"
    spacing: 10
    space_x: self.size[0]/3

    canvas.before:
        Color:
            rgba: (1, 1, 1, 1)
        Rectangle:
            source: 'black-friday-elements-assortment.jpg'
            size: root.width, root.height
            pos: self.pos

<BackgroundScreen>:
    name: 'background'
    MDRelativeLayout :
        MDIconButton:
            icon:'login.png'
            icon_size:"150sp"
            pos_hint:{'center_x' : 0.5,'center_y':0.8}
        MDTextField:
            id:user_name
            pos_hint:{'center_x':0.5,'center_y':0.5}
            size_hint:(0.7,0.1)
            hint_text:'username'
            helper_text:'Required'
            helper_text_mode:'on_error'
            icon_right:'account'
            required: True
            on_text: if self.text: self.hint_text = ''
        MDTextField:
            id:email 
            pos_hint:{'center_x':0.5,'center_y':0.4}
            size_hint:(0.7,0.1)
            hint_text:'email'
            helper_text:'Required'
            helper_text_mode:'on_error'
            icon_right:'account'
            required: True
            on_text: if self.text: self.hint_text = ''
        MDTextField:
            id:password
            pos_hint:{'center_x':0.5,'center_y':0.3}
            size_hint:(0.7,0.1)
            hint_text:'password'
            helper_text:'Required'
            helper_text_mode:'on_error'
            icon_right:'eye-off'
            required: True
            on_text: if self.text: self.hint_text = ''
            id:password
            pos_hint:{'center_x':0.5,'center_y':0.3}
            size_hint:(0.7,0.1)
            hint_text:'password'
            helper_text:'Required'
            helper_text_mode:'on_error'
            icon_right:'eye-off'
            required: True
            on_text: if self.text: self.hint_text = ''
        MDRaisedButton:
            name:'submit'
            pos_hint:{'center_x':0.5,'center_y':0.2}
            text: "SUBMIT"
            line_color: 0, 0, 0, 0
            on_press:app.check_username()
            on_release: app.switch_to_second_screen(self)
        MDTextButton:
            text: 'Already have an account ?'
            pos_hint: {'center_x':0.5,'center_y':0.15}
            # on_press: 
            #     root.manager.current = 'loginscreen'
            #     root.manager.transition.direction = 'down'

<SecondScreen>: 
    name: 'second'
    MDBoxLayout:
        orientation:"vertical"
        MDTopAppBar:
            MDRelativeLayout:
                MDTextField:
                    id:search_text
                    mode:"round"
                    hint_text: 'Search for Products'
                    size_hint:(0.9,1)
                    pos_hint: {'center_x':0.5,'center_y':0.95}
                    multiline:False
                    background_color:0,0,0,0
                    padding:15
                    on_text: if self.text: self.hint_text = ''
                    hint_text_color:rgba(206,206,209,255)
                MDIconButton:
                    icon:"magnify"
                    pos_hint: {'center_x':0.92,'center_y':0.95}
                    on_press:
                        app.search(search_text.text)     
        MDFloatLayout:
            MDLabel:
                text:" Snap-Deal:--Today's Deal"
                pos_hint:{"center_x":0.56,"center_y":0.8}
                font_style:'H6'
            MDLabel:
                text:" FlipKart Product:---Best OF Electronics "
                pos_hint:{"center_x":0.56,"center_y":0.42}
                font_style:'H6'
            ScrollView:
                do_scroll_y:False
                do_scroll_x:True
                pos_hint:{"center_y":0.62}
                size_hint_y:0.3
                bar_width:0
                GridLayout:
                    size_hint_x:None
                    height:2000
                    width:2000
                    rows:1
                    spacing:10
                    padding:18,0
                    MDIconButton:
                        id:product_name
                        icon_size:200
                        tooltip_text:""
                        theme_text_color:'Custom'
                        text_color:[1,1,1,1]
                        on_release:app.web_search(app.snap_link[0])
                        LoaderImage:
                            source:app.snap_img[0]
                            size:"500dp","500dp"
                    MDIconButton:
                        icon_size:200
                        theme_text_color:'Custom'
                        text_color:[1,1,1,1]
                        on_release:app.web_search(app.snap_link[1])
                        LoaderImage:
                            source:app.snap_img[1]
                            size:"500dp","500dp"
                    MDIconButton:
                        icon_size:200
                        theme_text_color:'Custom'
                        text_color:[1,1,1,1]
                        on_release:app.web_search(app.snap_link[2])
                        LoaderImage:
                            source:app.snap_img[2]
                            size:"500dp","500dp"
                    MDIconButton:
                        icon_size:200
                        theme_text_color:'Custom'
                        text_color:[1,1,1,1]
                        on_release:app.web_search(app.snap_link[3])
                        LoaderImage:
                            source:app.snap_img[3]
                            size:"500dp","500dp"
                    MDIconButton:
                        icon_size:200
                        theme_text_color:'Custom'
                        text_color:[1,1,1,1]
                        on_release:app.web_search(app.snap_link[4])
                        LoaderImage:
                            source:app.snap_img[4]
                            size:"500dp","500dp"
                    MDIconButton:
                        icon_size:200
                        theme_text_color:'Custom'
                        text_color:[1,1,1,1]
                        on_release:app.web_search(app.snap_link[5])
                        LoaderImage:
                            source:app.snap_img[5]
                            size:"500dp","500dp"
            ScrollView:
                do_scroll_y:False
                do_scroll_x:True
                pos_hint:{"center_y":0.22}
                size_hint_y:0.3
                bar_width:0
                GridLayout:
                    size_hint_x:None
                    height:2000
                    width:2000
                    rows:1
                    spacing:10
                    padding:18,0
                    MDIconButton:
                        id : 0
                        icon_size:200
                        theme_text_color:'Custom'
                        text_color:[1,1,1,1]
                        on_release: 
                            app.search_home(0)
                        LoaderImage:
                            source:app.flipkart_images[0]
                            size:"500dp","500dp"
                    MDIconButton:
                        id:1
                        icon_size:200
                        theme_text_color:'Custom'
                        text_color:[1,1,1,1]
                        on_release:app.search_home(1)
                        LoaderImage:
                            source:app.flipkart_images[1]
                            size:"500dp","500dp"
                    MDIconButton:
                        id:2
                        icon_size:200
                        theme_text_color:'Custom'
                        text_color:[1,1,1,1]
                        on_release:app.search_home(2)
                        LoaderImage:
                            source:app.flipkart_images[2]
                            size:"500dp","500dp"
                    MDIconButton:
                        id:3
                        icon_size:200
                        theme_text_color:'Custom'
                        text_color:[1,1,1,1]
                        on_release:app.search_home(3)
                        LoaderImage:
                            source:app.flipkart_images[3]
                            size:"500dp","500dp"
                    MDIconButton:
                        id:4
                        icon_size:200
                        theme_text_color:'Custom'
                        text_color:[1,1,1,1]
                        on_release:app.search_home(4)
                        LoaderImage:
                            source:app.flipkart_images[4]
                            size:"500dp","500dp"
                
<ThirdScreen>:
    name: 'third'
    MDIconButton:
        icon:"arrow-left"
        pos_hint:{"center_y":0.95}
        haligh:"center"
        on_release:
            root.manager.current='second'
            app.clear_results()

    MDLabel:
        id:search_label
        text:""     
        font_style:'H5'
        pos_hint:{"center_y":0.95}
        halign:"center"
    MDFloatLayout:
        MDLabel:
            text:" Snapdeal Product"
            pos_hint:{"center_x":0.56,"center_y":0.8}
            font_style:'H6'
        MDLabel:
            text:" FlipKart Product"
            pos_hint:{"center_x":0.56,"center_y":0.42}
            font_style:'H6'

        ScrollView:
            do_scroll_y:True
            do_scroll_x:True
            pos_hint:{"center_y":0.62}
            size_hint_y:0.3
            bar_width:0
            GridLayout:
                id:amazon_list
                size_hint_x:None
                height:2000
                width:2000
                rows:1
                spacing:10
                padding:18,0

        ScrollView:
            do_scroll_y:True
            do_scroll_x:True
            size_hint_y:0.9
            pos_hint:{"center_x":0.5,"center_y":-0.1}
            bar_width:0
            GridLayout:
                id:flipkart_list
                size_hint_x:None
                height:2000
                width:2000
                rows:1
                spacing:10
                padding:18,0

<ProductInfo>:
    name:'product'
    MDIconButton:
        icon:"arrow-left"
        pos_hint:{"center_y":0.95}
        haligh:"center"
        on_release:
            root.manager.current='third'
            app.clear_window()

    BoxLayout:
        id:product_box
        orientation: 'horizontal'
        spacing: dp(10)
        padding: dp(10) 
    BoxLayout:
        id:price
        orientation: 'horizontal'
        spacing: dp(10)
        padding: dp(10)
    BoxLayout:
        id:buy_link
        orientation: 'horizontal'
        spacing: dp(10)
        padding: dp(10)

    MDRaisedButton:
        pos_hint:{'center_x':0.5,'center_y':0.2}
        text: "REVIEWS"
        line_color: 0, 0, 0, 0
        on_press:
            root.manager.current='review'

            app.on_review_click_flipkart(self)

<ReviewScreen>:
    name: 'review'
    MDIconButton:
        icon:"arrow-left"
        pos_hint:{"center_y":0.95}
        haligh:"center"
        on_release:
            root.manager.current='product' 
            app.clear_review()

    MDLabel:
        text:"REVIEWS WITH SENTIMENT"     
        font_style:'H5'
        pos_hint:{"center_y":0.95}
        halign:"center"    
    BoxLayout:
        id:rev
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)   


'''
class LoaderImage(AsyncImage):
      Loader.loading_image="1495.gif"
class Background(MDRelativeLayout):
    pass
class NavigationDrawerIconButton(Button):
    pass
class TooltipMDIconButton(MDIconButton, MDTooltip):
    pass
class BackgroundScreen(Screen):
    pass
class MDToolbar(MDToolbar):
    pass
class SecondScreen(Screen):
     pass
class ThirdScreen(Screen):
    pass
class ProductInfo(Screen):
    pass
class ReviewScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(BackgroundScreen(name='background'))
sm.add_widget(SecondScreen(name='second'))
sm.add_widget(ThirdScreen(name='third'))
sm.add_widget(ProductInfo(name='product'))
sm.add_widget(ReviewScreen(name='review'))
class NewApp(MDApp):
    def build(self):
        self.url="https://loginsystem-3e0e7-default-rtdb.firebaseio.com/.json"
        self.flipkart_data=self.flipkart_deal()
        self.flipkart_images=self.flipkart_data['url']
        self.flipkart_deal_names=self.flipkart_data['name']
        self.snap_deal_data=self.snap_deal()
        self.snap_img=self.snap_deal_data['url']
        self.snap_link=self.snap_deal_data['link']
        self.strng = Builder.load_string(helpstr)
        return self.strng
    def check_username(self):
        self.username_text = self.strng.get_screen('background').ids.user_name.text
        self.email_id=self.strng.get_screen('background').ids.email.text
        self.password_text=self.strng.get_screen('background').ids.password.text
        self.username_check_false = True
        try:
            int(self.username_text)
        except:
            self.username_check_false = False
        if self.username_check_false or self.username_text.split() == [] or len(self.username_text.split())>1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry',on_release=self.close_username_dialogue)
            self.dialog = MDDialog(title='Invalid Username', text="Please input a valid username", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            self.strng.get_screen('background').ids.submit = False
            signupinfo=str('{{"{email}":{{"password":"{password}","username":"{username}"}}}}'.format(email=self.email_id, password=self.password_text, username=self.username_text))
            signupinfo=signupinfo.replace(".","-")
           #  to_database= json.loads(signupinfo)
           #  print(to_database)
           #  requests.patch(url=self.url,json=to_database,headers = ({
           # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46"}))
        return self.username_check_false
    def search(self,search_text):
        if search_text!="":
            self.strng.get_screen('third').ids.search_label.text=search_text
            self.root.current = 'third'
            self.product_name=self.strng.get_screen('second').ids.search_text.text
            self.data=self.flipkart_product_name(search_text=self.product_name)
            self.amazon_data = self.amazon_product_name(search_text=self.product_name)
            self.amazon_name = self.amazon_data['name']
            self.amazon_prices = self.amazon_data['prices']
            self.amazon = self.amazon_data['url']
            self.amazon_link = self.amazon_data['page_link']
            self.names = self.data['name']
            self.prices = self.data['prices']
            self.flipt = self.data['url']
            self.links = self.data['page_link']
            for p in range(0, len(self.amazon)):
                button = MDIconButton(
                    icon_size=200,
                    theme_text_color='Custom',
                    text_color=[1, 1, 1, 1],
                    #on_click=self.web_search(self.amazon_link[p])
                )
                button.add_widget(LoaderImage(source=self.amazon[p]))
                self.strng.get_screen('third').ids.amazon_list.add_widget(button)

            for i in range(0,len(self.flipt)):
                button = MDIconButton(
                    icon_size=200,
                    theme_text_color='Custom',
                    text_color=[1, 1, 1, 1],
                    on_release=lambda instance, i=i,root=self.root,strng=self.strng,names=self.names,price=self.prices,link=self.links: (self.on_button_click_wrapper(index=i,root=root,strng=strng,names=names,price=price,link=link)(instance),self.add_to_review_list_flipkart(i))
                )
                button.add_widget(LoaderImage(source=self.flipt[i]))  # set the image as the background
                self.strng.get_screen('third').ids.flipkart_list.add_widget(button)

    def search_home(self,x):
        self.strng.get_screen('third').ids.search_label.text = self.flipkart_deal_names[x]
        self.root.current = 'third'
        self.product_name=self.flipkart_deal_names[x]
        self.data = self.flipkart_product_name(search_text=self.product_name)
        self.amazon_data = self.amazon_product_name(search_text=self.product_name.split(' ')[0])
        self.amazon_name = self.amazon_data['name']
        self.amazon_prices = self.amazon_data['prices']
        self.amazon= self.amazon_data['url']
        self.amazon_link=self.amazon_data['page_link']
        self.names = self.data['name']
        self.prices = self.data['prices']
        self.flipt=self.data['url']
        self.links = self.data['page_link']
        for p in range(0, len(self.amazon)):
            button = MDIconButton(
                icon_size=200,
                theme_text_color='Custom',
                text_color=[1, 1, 1, 1],
                #on_click=self.web_search(self.amazon_link[p])
            )
            button.add_widget(LoaderImage(source=self.amazon[p]))  # set the image as the background
            self.strng.get_screen('third').ids.amazon_list.add_widget(button)
        for i in range(0, len(self.flipt)):
            button = MDIconButton(
                icon_size=200,
                theme_text_color='Custom',
                text_color=[1, 1, 1, 1],
                on_release=lambda instance, i=i, root=self.root, strng=self.strng, names=self.names, price=self.prices,
                                  link=self.links: (
                self.on_button_click_wrapper(index=i, root=root, strng=strng, names=names, price=price, link=link)(
                    instance), self.add_to_review_list_flipkart(i))
            )
            button.add_widget(LoaderImage(source=self.flipt[i]))  # set the image as the background
            # add the button to your widget tree
            self.strng.get_screen('third').ids.flipkart_list.add_widget(button)
    def search_amazon(self,x):
        webbrowser.open(self.amazon_link[x])
    def close_username_dialogue(self, obj):
        self.dialog.dismiss()

    def add_to_review_list_flipkart(self, index):
        self.reviews= self.flipkart_reviews(index=index)

    def add_to_review_list_amazon(self, index):
        self.amazon_rev=self.amazon_reviews(index=index)
    def on_button_click_wrapper(self, index, root, strng, names, price, link):
        def on_button_click(instance, self=self):
            root.current = 'product'
            root.transition.direction = 'right'
            named = MDLabel(
                text="NAME :",
                pos_hint={"center_x": 0.0, "center_y": 0.78}
            )
            strng.get_screen('product').ids.product_box.add_widget(named)
            label = MDLabel(
                text=names[index],
                pos_hint={"center_x": 0.4, "center_y": 0.78}
            )
            strng.get_screen('product').ids.product_box.add_widget(label)
            label = MDLabel(
                text="PRICE :",
                pos_hint={"center_x": 0.0, "center_y": 0.60}
            )
            strng.get_screen('product').ids.price.add_widget(label)
            label = MDLabel(
                text=price[index],
                pos_hint={"center_x": 0.4, "center_y": 0.60}
            )
            strng.get_screen('product').ids.price.add_widget(label)
            label = MDLabel(
                text="BUY LINK :",
                pos_hint={"center_x": 0.0, "center_y": 0.40}
            )
            strng.get_screen('product').ids.buy_link.add_widget(label)
            label = MDTextButton(
                text='CLICK HERE',
                pos_hint={"center_x": 0.4, "center_y": 0.40},
                on_press=lambda instance, link=link[index]: webbrowser.open(link)
            )
            strng.get_screen('product').ids.buy_link.add_widget(label)

        return lambda instance: on_button_click(instance, self)

    def on_review_click_flipkart(self, instance):
        self.root.current = 'review'
        rev = self.reviews
        if len(rev) != 0:
            table = MDDataTable(pos_hint={"center_x": 0.5, "center_y": 0.3}, size_hint= (0.9, 1), check=False, rows_num=len(rev),
                                column_data=[("REVIEWS", dp(150)), ("SENTIMENT", dp(10))]
                                , row_data=[(i, self.sentiment_analysis(i)) for i in rev] + [("")] * 3)
            self.strng.get_screen('review').ids.rev.add_widget(table)
        else:
            cancel_btn_review = MDFlatButton(text='Retry Some Other Products', on_release=self.close_review_dialogue)
            self.review_diag = MDDialog(title='NO Reviews', text="No Reviews Available For This Product Or You Can Check the Website by clicking on BUY LINK", size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_review])
            self.review_diag.open()

    def close_review_dialogue(self, obj):
        self.review_diag.dismiss()

    def on_review_click_snapdeal(self, instance):
        self.root.current = 'review'
        rev = self.reviews
        if len(rev) != 0:
            table = MDDataTable(id='table',pos_hint={"center_x": 0.5, "center_y": 0.3}, size_hint=(0.9, 0.5), check=False,
                                rows_num=len(rev),
                                column_data=[("REVIEWS", dp(50)), ("SENTIMENT", dp(50))]
                                , row_data=[(i, self.sentiment_analysis(i)) for i in rev] + [("")] * 3)
            self.strng.get_screen('review').ids.rev.add_widget(table)
        else:
            label = MDLabel(text="SORRY SIR THERE IS NO REVIEWS FOR THIS PRODUCT",
                            pos_hint={"center_x": 0.5, "center_y": 0.3})
            self.strng.get_screen('review').ids.rev.add_widget(label)
    def emojis(self,sentiment):
        positive_emoji = "\U0001F600"  # Grinning Face
        negative_emoji = "\U0001F61E"  # Disappointed Face
        neutral_emoji = "\U0001F610"  # Neutral Face
        if sentiment == 1:
            emoji = positive_emoji
        elif sentiment == -1:
            emoji = negative_emoji
        else:
            emoji = neutral_emoji
        return emoji
    def check_press(self,instance,table,current_row):
        pass
    def row_press(self,instance,table,current_row):
        pass
    def switch_to_second_screen(self, instance):
        if (self.username_check_false== False and self.username_text.isspace()==False and len( self.username_text)!=0 ) :
            self.root.current = 'second'
            self.root.transition.direction = 'right'
    def on_button_click(self,instance):
            pass
    def callback(self,search_text=''):
        import re
        if search_text != "":
            url = f"https://www.techbargains.com/search?search={search_text}"
            headers = ({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46"})
            r = requests.get(url, headers=headers)
            htmlcontent = r.content
            soup = BeautifulSoup(htmlcontent, 'lxml')
            divs = soup.find_all('div', {'class': 'col-sm-4 text-center text-sm-left my-2 my-sm-0 pb-2'})
            names = []
            prices = []
            url = []
            img_url = []
            for it in divs:
                img = it.find('img', {'class': 'img-fluid'})
                img_url.append(img['src'])
                names.append(img['alt'])
                page_link = it.find('a')
                url.append(page_link)
                text = img['alt']
                price_pattern = r'\$(\d+(\.\d{1,2})?)'
                match = re.search(price_pattern, text)
                if match:
                    price = match.group(0)
                    prices.append(price)
                else:
                    text = img['alt']
                    percentage_pattern = r'Up to (\d+)%'
                    match = re.search(percentage_pattern, text)
                    if match:
                        percentage = match.group(0)
                        prices.append(percentage)

        df = pd.DataFrame({'name': names, 'prices': prices, 'url': img_url, 'page_link': url})
        return df
    def amazon_product_name(self,search_text=""):
        import re
        if search_text != "":
            url = f"https://www.techbargains.com/search?search={search_text}"
            headers = ({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46"})
            r = requests.get(url, headers=headers)
            htmlcontent = r.content
            soup = BeautifulSoup(htmlcontent, 'html.parser')
            divs = soup.find_all('div', {'class': 'col-sm-4 text-center text-sm-left my-2 my-sm-0 pb-2'})
            names = []
            prices = []
            url = []
            img_url = []
            for it in divs:
                img = it.find('img', {'class': 'img-fluid'})
                img_url.append(img['src'])
                names.append(img['alt'])
                page_link = it.find('a')
                url.append(page_link['href'])
                text = img['alt']
                price_pattern = r'\$(\d+(\.\d{1,2})?)'
                match = re.search(price_pattern, text)
                if match:
                    price = match.group(0)
                    prices.append(price)
                else:
                    text = img['alt']
                    percentage_pattern = r'Up to (\d+)%'
                    match = re.search(percentage_pattern, text)
                    if match:
                        percentage = match.group(0)
                        prices.append(percentage)

        df = pd.DataFrame({'name': names, 'prices': prices, 'url': img_url, 'page_link': url})
        return df
    def flipkart_deal(self):
        url = "https://www.flipkart.com"
        headers = ({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46"})
        r = requests.get(url, headers=headers)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        images = soup.find_all('img', {'class': '_396cs4'})
        img_names=soup.find_all('div',{'class':'_3LU4EM'})
        images_url = []
        names = []
        for image in images:
            images_url.append(image['src'])
            names.append(image['alt'].split('(')[0])
        img_url = images_url[10:]
        names = names[10:]
        df=pd.DataFrame({'name':names,'url':img_url})
        return df
    def snap_deal(self):
        import requests
        from bs4 import BeautifulSoup
        import pandas as pd
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        r = requests.get(url='https://www.snapdeal.com/', headers=headers)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        divs = soup.find_all('div', {'class': 'trendingProd product-relative dp-widget-link col-xs-5 favDp'})
        links = []
        imgs = []
        for i in divs:
            link = i.find('a', {'class': 'product-card dp-widget-link'})
            links.append(link['href'])
            div_img = link.find('div', {'class': 'product-img'})
            img = div_img.find('img', {'class': 'lazy-load'})
            imgs.append(img['data-src'])
        df=pd.DataFrame({'url':imgs,'link':links})
        return df
    def clear_results(self):
        self.strng.get_screen('second').ids.search_text.text=""
        self.strng.get_screen('third').ids.amazon_list.clear_widgets()
        self.strng.get_screen('third').ids.flipkart_list.clear_widgets()
    def web_search(self,link):
        webbrowser.open(link)
    def clear_window(self):
        self.strng.get_screen('product').ids.product_box.clear_widgets()
        self.strng.get_screen('product').ids.price.clear_widgets()
        self.strng.get_screen('product').ids.buy_link.clear_widgets()
    def clear_review(self):
        self.strng.get_screen('review').ids.rev.clear_widgets()
    def flipkart_product_name(self,search_text):
        import pandas as pd
        import requests
        from bs4 import BeautifulSoup
        if search_text != '':
            url = f"https://www.flipkart.com/search?q={search_text}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
            headers = ({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46"})
            r = requests.get(url, headers=headers)
            htmlcontent = r.content
            soup = BeautifulSoup(htmlcontent, 'html.parser')
            # if search_text=='camera' or search_text=='laptops':
            name = []
            prices = []
            img_url = []
            links = []
            link = soup.find_all('a', {'class': '_1fQZEK'})
            for i in link:
                links.append('https://www.flipkart.com' + i['href'])
                x = i.find('div', {'class': 'CXW8mj'})
                p = x.find('img', {'class': '_396cs4'})
                price = i.find('div', {'class': '_30jeq3 _1_WHN1'})
                name.append(p['alt'])
                img_url.append(p['src'])
                prices.append(price.text)
            df = pd.DataFrame({'name': name, 'prices': prices, 'url': img_url, 'page_link': links})
        return df


    def flipkart_reviews(self,index):
        self.links=self.data['page_link'][index]
        headers = ({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46"})


        r1 = requests.get(self.links, headers)
        htmlcontent = r1.content
        soup1 = BeautifulSoup(htmlcontent, 'html.parser')
        rev = soup1.find_all('div', {'class': 't-ZTKy'})
        revx = []
        for r in rev:
            revx.append(r.text)
        return revx
    def clean_html(self,text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def convert_lower(self,text):
        return text.lower()

    def remove_special(self,text):
        x = ''
        for i in text:
            if i.isalnum():
                x = x + i
            else:
                x = x + ' '
        return x

    def remove_stopwords(self,text):
        x = []
        for i in text.split():
            if i not in stopwords.words('english'):
                x.append(i)
        y = x[:]
        x.clear()
        return y

    def stem_words(self,text):
        ps=nltk.PorterStemmer()
        y=[]
        for i in text:
            y.append(ps.stem(i))
        z = y[:]
        y.clear()
        return z
    def remove_emojis(self,text):
        # Define the regex pattern for emojis
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002500-\U00002BEF"  # chinese char
                                   u"\U00002702-\U000027B0"
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   u"\U0001f926-\U0001f937"
                                   u"\U00010000-\U0010ffff"
                                   u"\u2640-\u2642"
                                   u"\u2600-\u2B55"
                                   u"\u200d"
                                   u"\u23cf"
                                   u"\u23e9"
                                   u"\u231a"
                                   u"\ufe0f"  # dingbats
                                   u"\u3030"
                                   "]+", flags=re.UNICODE)

        # Remove emojis from the text
        text_no_emoji = emoji_pattern.sub(r'', text)
        return text_no_emoji
    def join_back(self,list_input):
        return " ".join(list_input)
    def sentiment_analysis(self,review):
        text=self.clean_html(review)
        text=self.convert_lower(text)
        text=self.remove_special(text)
        text=self.remove_emojis(text)
        text=text.replace('readmore','')
        text=self.stem_words(text)
        text=self.join_back(text)
        with open('Sentiments.pkl', 'rb') as file:
            model = pickle.load(file)
        number=model.predict([text])
        return number

NewApp().run()
