import asyncio
import os
from backboard import BackboardClient

API_KEY = "espr_d50PVrO-aeKDSsReBXf5Au76XGu5sZFFrHEqbW8b5bs"

async def main():
    client = BackboardClient(api_key=API_KEY)
    
    try:
        print("Creating Assistant...")
        assistant = await client.create_assistant(
            name="My First Assistant",
            description="You are a helpful assistant that responds concisely."
        )
        print(f"✅ Created assistant: {assistant.assistant_id}")

        print("Creating Thread...")
        thread = await client.create_thread(assistant.assistant_id)
        print(f"✅ Created thread: {thread.thread_id}")

        print("Sending message...")
        response = await client.add_message(
            thread_id=thread.thread_id,
            content="say Hello World",
            stream=False
        )
        print(f"🤖 Assistant: {response.content}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())