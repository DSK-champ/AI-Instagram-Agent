"""
Feed Customiser Agent
Automates customizing Instagram explore feed based on user interests.
"""

from droidrun import DroidAgent
from config import create_config


def create_feed_customiser_prompt(user_preferences: str) -> str:
    """
    Create the feed customiser prompt with user preferences.
    
    Args:
        user_preferences: Comma-separated list of user interests (e.g., "Educational, Funny, Marvel edits")
    
    Returns:
        str: Formatted prompt for the agent
    """
    return f"""You are an AI agent that customizes the Instagram feed based on USER INTERESTS.

FUNCTION: Train the explore feed by actively searching and liking relevant content.

━━━━━━━━━━━━━━━━━━━━━━━
🎯 GOAL
━━━━━━━━━━━━━━━━━━━━━━━
User gives preferences →  
Search relevant content →  
Like 10 continuous posts/reels →  
Return summary.

━━━━━━━━━━━━━━━━━━━━━━━
1️⃣ INPUT FROM USER
━━━━━━━━━━━━━━━━━━━━━━━

User Preference: {user_preferences}

━━━━━━━━━━━━━━━━━━━━━━━
2️⃣ OPEN INSTAGRAM
━━━━━━━━━━━━━━━━━━━━━━━

- Tap 📸 Instagram icon  
- Wait for home screen.
- If you are already in instagram, navigate to search icon.

━━━━━━━━━━━━━━━━━━━━━━━
3️⃣ GO TO SEARCH
━━━━━━━━━━━━━━━━━━━━━━━

- Tap 🔍 Search icon (bottom navbar).  
- Tap top SEARCH BAR.

━━━━━━━━━━━━━━━━━━━━━━━
4️⃣ FOR EACH USER INTEREST
━━━━━━━━━━━━━━━━━━━━━━━

FOR every keyword in preference list:

   a. Type keyword  
      Example: "Marvel edits"

   b. Open first relevant result.

━━━━━━━━━━━━━━━━━━━━━━━
5️⃣ TRAIN FEED BY LIKING
━━━━━━━━━━━━━━━━━━━━━━━

REPEAT 10 TIMES:

   - Open first reel/post    
   - Tap ❤️ Like icon as early as you can
   - Swipe up to next reel

━━━━━━━━━━━━━━━━━━━━━━━
6️⃣ MULTI-CATEGORY LOGIC
━━━━━━━━━━━━━━━━━━━━━━━

If user gave:

Educational → search  
- "science facts"  
- "coding tips"  
- "history facts"

Funny →  
- "indian memes"  
- "college memes"

Marvel edits →  
- "marvel edits"  
- "avengers edit"

━━━━━━━━━━━━━━━━━━━━━━━
7️⃣ SAFETY
━━━━━━━━━━━━━━━━━━━━━━━

- Avoid adult content  
- Avoid hate content  
- Skip political extremism

━━━━━━━━━━━━━━━━━━━━━━━
8️⃣ EXIT
━━━━━━━━━━━━━━━━━━━━━━━

- After 10 likes →  
  Tap 🔙 Back to search  
- Continue for next interest.

━━━━━━━━━━━━━━━━━━━━━━━
📦 OUTPUT JSON
━━━━━━━━━━━━━━━━━━━━━━━

{{
  "preferences": [],
  "searched_keywords": [],
  "posts_liked": 10,
  "status": "completed"
}}"""


async def run_feed_customiser(user_preferences: str):
    """
    Run the Feed Customiser agent to customize Instagram explore feed.
    
    Args:
        user_preferences: Comma-separated list of interests (e.g., "Educational, Funny, Marvel edits")
    
    Returns:
        Result object from the agent execution
    """
    config = create_config(max_steps=100)  # More steps for multiple searches
    
    goal = create_feed_customiser_prompt(user_preferences)
    
    agent = DroidAgent(
        goal=goal,
        config=config,
    )
    
    result = await agent.run()
    return result
