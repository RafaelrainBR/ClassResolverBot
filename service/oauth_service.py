from __future__ import print_function

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = ['https://www.googleapis.com/auth/classroom.courses.readonly']


def create_flow():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials/credentials.json', scopes)

    flow.redirect_uri = 'https://discord.com/channels/@me'
    return flow


def get_authorization_url(flow):
    return flow.authorization_url()


def get_courses(credentials):
    service = build('classroom', 'v1', credentials=credentials)
    results = service.courses().list(pageSize=15).execute()

    courses = results.get('courses', [])

    return courses
