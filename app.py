import os
import evernote.edam.type.ttypes as Types
import twilio.twiml

from flask import Flask, redirect, url_for, request
from evernote.api.client import EvernoteClient

app = Flask(__name__)

auth_token = os.environ.get('EVERNOTE_AUTH_TOKEN')

client = EvernoteClient(token=auth_token, sandbox=False)

note_store = client.get_note_store()

@app.route('/', methods=['POST'])
def index():
    create_note(
        title='Text2Note from {0}'.format(request.values.get('From', 'unknown number')),
        content=request.values.get('Body')
    )
    return sms("Note created.")

def create_note(title, content):
    note = Types.Note()
    note.title = title
    note.content = note_enml(content)
    return note_store.createNote(note)

def note_enml(content):
    return '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd"><en-note>{0}</en-note>'.format(content)

def sms(content):
    response = twilio.twiml.Response()
    response.sms(content)
    return str(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
