import os
from supabase_py import create_client, Client

from model.chat import Message, Conversation

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def add_conversation(user_id) -> dict:
    conversation = Conversation(user_id)
    data = supabase.table("conversations").insert(conversation.to_dict()).execute()
    print(data)
    return data['data']


def add_message(conversation_id, user_id, message_text) -> dict:
    message = Message(conversation_id, user_id, message_text)
    data = supabase.table("messages").insert(message.to_dict()).execute()
    print(data)
    return data['data']


def get_conversations_from_db(user_id) -> dict:
    data = supabase.table("conversations").select("*").eq("user_id", user_id).execute()
    return data['data']


def get_messages_from_db(conversation_id) -> dict:
    data = supabase.table("messages").select("*").eq("conversation_id", conversation_id).execute()
    return data['data']
