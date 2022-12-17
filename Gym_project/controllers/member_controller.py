from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym import Gym
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

member_blueprint = Blueprint('mamber',__name__)