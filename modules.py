import json
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from config import KV
from kivy.network.urlrequest import UrlRequest
from kivy.properties import StringProperty
import requests
from kivy.clock import Clock