from flask import Flask, render_template, request, redirect, url_for, session
import PSQLFunc as p


def find_userID(identifier):
    user_id = p.insert_data(identifier, request.get_json()[identifier])
    return user_id
