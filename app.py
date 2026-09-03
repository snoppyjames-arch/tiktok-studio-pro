from flask import Flask, request, jsonify, render_template_string
import urllib.parse
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TikTok Studio Pro - SUPER FREE</title>
<style>
body{font-family:Arial;background:#000;color:#fff;padding:15px;margin:0}
h1{color:#ff0050;text-align:center;font-size:24px}
.input-box{width:100%;padding:15px;font-size:16px;border-radius:10px;border:2px solid #ff0050;background:#111;color:#fff;box-sizing:border-box}
.btn{width:100%;padding:18px;background:linear-gradient(45deg,#ff0050,#00f2ea);border:none;border-radius:12px;color:#fff;font-size:18px;font-weight:bold;margin-top:15px;cursor:pointer}
.card{background:#111;border:1px solid #333;border-radius:12px;padding:15px;margin-top:15px}
.card h3{color:#00f2ea;margin-top:0
