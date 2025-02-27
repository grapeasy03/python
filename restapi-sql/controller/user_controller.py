from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from app import app
from model.user_model import user_model
from flask import request
from flask import make_response

obj=user_model()

@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()


@app.route('/user/addone',methods=["POST"])
def user_addone_controller():
    # print(request.form)
    return obj.user_addone_model(request.form)


# put
@app.route('/user/update',methods=["PUT"])
def user_update_controller():
    # print(request.form)
    return obj.user_update_model(request.form)

# @app.route('/user/delete',methods=["DELETE"])
# def user_delete_controller():
#     return obj.user_delete_model(request.form)

@app.route('/user/delete',methods=["DELETE"])
def user_delete_controller():
    return obj.user_delete_model(request.form)

@app.route("/user/patch/<id>",methods=["PATCH"])
def user_patch_controller(id):
    return obj.user_patch_model(request.form,id)

