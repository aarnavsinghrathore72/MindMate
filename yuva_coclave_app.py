import streamlit as st
import random 
import time
import datetime
from collections import deque
import pandas as pd
import plotly.graph_objects as go

# -------- Mental Health Assessment Library --------
mental_health_assessment = {
    "mood": {
        "low": """
😔 **You've been feeling low lately — that's completely human and valid.**

### 🌱 Gentle Steps to Lift Your Mood:

1. **Start with micro-moments of joy:**
   - Watch 1 funny animal video 🐶
   - Listen to your favorite childhood song 🎵
   - Step outside for 3 deep breaths of fresh air 🌿

2. **The 5-4-3-2-1 Grounding Technique:**
   - **5** things you can see
   - **4** things you can touch
   - **3** things you can hear
   - **2** things you can smell
   - **1** thing you can taste

3. **Create a "Feel Good" Playlist:**
   - 5 songs that make you smile
   - Listen during your shower or commute

4. **Movement Magic:**
   - 5-minute gentle stretching
   - Dance to one song (no one watching!)
   - Walk around the block noticing colors

### 📱 Digital Tools:
- **Gratitude apps:** Presently, Gratitude Garden
- **Mood tracking:** Daylio, How We Feel
- **Gentle reminders:** Finch (self-care pet)

💖 *Your feelings are visitors—let them come, let them stay, let them leave when ready.*
""",

        "moderate": """
😌 **You're managing okay, but could use some emotional TLC.**

### 🧘‍♀️ Level Up Your Emotional Wellness:

1. **Daily Mindfulness Rituals:**
   - Morning: 3 things you're grateful for
   - Afternoon: 1-minute breathing space
   - Evening: Reflect on 1 small win

2. **Digital Detox Zones:**
   - No phone first 30 minutes after waking
   - Screen-free dinner time
   - Charge phone outside bedroom

3. **Creative Expression:**
   - Doodle without purpose for 5 minutes
   - Write a haiku about your day
   - Take photos of things that catch your eye

4. **Social Connection:**
   - Send 1 "thinking of you" text
   - Video call with someone who energizes you
   - Join a virtual book club or hobby group

### 🌈 Resources:
- **Meditation:** Insight Timer (free), Calm
- **Journaling:** Journey, Penzu
- **Community:** 7 Cups (peer support)

✨ *Wellness isn't a destination—it's the quality of your journey.*
""",

        "high": """
🌟 **Your positive energy is shining! Let's keep this momentum going.**

### 🚀 Deepening Your Emotional Resilience:

1. **Purposeful Positivity:**
   - Mentor someone in your area of strength
   - Start a positivity journal to share insights
   - Create "mental health first aid" kits for friends

2. **Advanced Mindfulness:**
   - Try loving-kindness meditation
   - Practice walking meditation in nature
   - Start a gratitude jar with daily notes

3. **Preventive Self-Care:**
   - Design your ideal weekly wellness schedule
   - Learn about emotional intelligence skills
   - Explore therapy for maintenance (not just crisis)

4. **Community Impact:**
   - Volunteer for mental health organizations
   - Share your wellness journey anonymously
   - Start a workplace mental health initiative

### 🔥 Growth Resources:
- **Books:** "The Happiness Trap", "Daring Greatly"
- **Courses:** Yale's Science of Wellbeing (free)
- **Advanced:** ACT therapy, Positive Psychology

🎯 *Your light can illuminate paths for others too.*
"""
    },

    "stress": {
        "low": """
😊 **You're handling stress well! Keep these protective habits.**

### 🛡️ Stress Prevention Strategies:

1. **Maintenance Routines:**
   - Weekly "stress audit" - what worked/didn't?
   - Keep a "worry time" (15 min/day only)
   - Regular digital detox days

2. **Resilience Building:**
   - Practice saying "no" to one thing weekly
   - Develop a "stress first aid" kit
   - Learn progressive muscle relaxation

3. **Preventive Self-Care:**
   - Schedule quarterly mental health days
   - Regular nature immersion
   - Keep learning about emotional wellness

### 📚 Resources:
- **Stress tracking apps:** Worry Watch
- **Resilience:** Headspace, Ten Percent Happier
- **Books:** "Why Zebras Don't Get Ulcers"

🛡️ *Prevention is the most elegant form of healing.*
""",

        "moderate": """
😟 **Stress is knocking — time for some intentional unwinding.**

### 🧘 Immediate Stress Relief:

1. **Quick Reset Techniques:**
   - Box breathing: 4s inhale, 4s hold, 4s exhale
   - 5-minute guided body scan
   - Cold water splash on face

2. **Stress Buffer Activities:**
   - Nature walk (no phone)
   - Coloring or puzzle for 15 minutes
   - Listen to binaural beats or calm music

3. **Boundary Setting:**
   - Delegate one task today
   - Turn off non-essential notifications
   - Create "no stress zones" at home

4. **Physical Release:**
   - Shake out tension (literally!)
   - Gentle yoga or stretching
   - Progressive muscle relaxation

### 🆘 Quick Help:
- **Breathing apps:** Breathe2Relax
- **Calm spaces:** Noisli (ambient sounds)
- **Crisis text:** Text HOME to 741741

🌊 *You can't stop the waves, but you can learn to surf.*
""",

        "high": """
😰 **Stress is overwhelming right now — let's create calm together.**

### 🆘 Emergency Stress Protocol:

1. **Immediate Grounding:**
   - **5-4-3-2-1 Technique** (see, touch, hear, smell, taste)
   - Hold ice cube in hand for 30 seconds
   - Strong mint or sour candy for sensory focus

2. **Safety Planning:**
   - Remove yourself from stress source if possible
   - Call/text a trusted person (pre-arranged)
   - Visit calming space (bathroom, quiet room)

3. **Body Calming:**
   - Butterfly hug (cross arms, tap shoulders)
   - Hum or sing (vibration calms nervous system)
   - Gentle rocking or swaying

4. **Professional Support:**
   - Crisis hotline: 988 or your local number
   - Urgent care if needed
   - Schedule therapy appointment

### 🚨 Emergency Resources:
- **National:** 988 Suicide & Crisis Lifeline
- **Text:** Crisis Text Line (741741)
- **International:** Find your country's line

🤝 *You don't have to carry this alone. Reach out, right now.*
"""
    }
}

# -------- SDG Integration --------
SDG_INFO = {
    3: {
        "title": "GOOD HEALTH AND WELL-BEING",
        "description": "Ensure healthy lives and promote well-being for all at all ages",
        "targets": [
            "Target 3.4: Reduce premature mortality from non-communicable diseases through prevention and treatment",
            "Target 3.5: Strengthen the prevention and treatment of substance abuse",
            "Target 3.8: Achieve universal health coverage"
        ],
        "color": "#4C9F38",
        "icon": "🏥"
    },
    4: {
        "title": "QUALITY EDUCATION",
        "description": "Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all",
        "targets": [
            "Target 4.7: Education for sustainable development and global citizenship",
            "Target 4.4: Increase skills for employment and entrepreneurship"
        ],
        "color": "#C5192D",
        "icon": "🎓"
    },
    8: {
        "title": "DECENT WORK AND ECONOMIC GROWTH",
        "description": "Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all",
        "targets": [
            "Target 8.5: Achieve full and productive employment and decent work for all",
            "Target 8.6: Reduce youth unemployment"
        ],
        "color": "#A21942",
        "icon": "💼"
    },
    10: {
        "title": "REDUCED INEQUALITIES",
        "description": "Reduce inequality within and among countries",
        "targets": [
            "Target 10.2: Promote social, economic and political inclusion"
        ],
        "color": "#DD1367",
        "icon": "⚖️"
    }
}

# -------- Helper Functions --------
def classify(score):
    if score >= 70:
        return "high"
    elif score >= 40:
        return "moderate"
    else:
        return "low"

def create_mood_chart(days=7):
    """Create animated mood chart"""
    fig = go.Figure()
    
    # Sample data
    days_list = [f'Day {i}' for i in range(1, days+1)]
    mood_scores = [random.randint(30, 90) for _ in range(days)]
    
    fig.add_trace(go.Scatter(
        x=days_list,
        y=mood_scores,
        mode='lines+markers',
        name='Mood Score',
        line=dict(color='#FF6B6B', width=4),
        marker=dict(size=10, color='#FFD93D'),
        fill='tozeroy',
        fillcolor='rgba(255, 107, 107, 0.2)'
    ))
    
    fig.update_layout(
        title="📈 Your Mood Journey",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        hovermode='x unified'
    )
    
    return fig

# -------- Pages --------
def welcome_page():
    st.markdown("""
        <style>
        @keyframes gradient {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        
        .welcome-container {
            background: linear-gradient(-45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
            color: white;
            padding: 60px 40px;
            border-radius: 30px;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
            border: 3px solid rgba(255,255,255,0.2);
        }
        
        .welcome-container::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: float 20s linear infinite;
        }
        
        @keyframes float {
            0% {transform: translate(0, 0) rotate(0deg);}
            100% {transform: translate(-50px, -50px) rotate(360deg);}
        }
        
        .welcome-container h1 {
            font-size: 4.5rem;
            margin-bottom: 15px;
            font-weight: 900;
            text-shadow: 3px 3px 0 rgba(0,0,0,0.2);
            background: linear-gradient(45deg, #FFD93D, #FF6B6B);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -1px;
        }
        
        .welcome-container h3 {
            font-size: 2.2rem;
            margin-bottom: 30px;
            font-weight: 600;
            color: #1A1A2E;
            text-shadow: 2px 2px 4px rgba(255,255,255,0.3);
        }
        
        .welcome-container p {
            font-size: 1.4rem;
            line-height: 1.8;
            margin-bottom: 30px;
            background: rgba(26, 26, 46, 0.8);
            padding: 25px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255,255,255,0.1);
        }
        
        .welcome-points {
            background: rgba(255, 255, 255, 0.15);
            padding: 25px;
            border-radius: 20px;
            margin: 30px auto;
            font-size: 1.3rem;
            text-align: left;
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255,255,255,0.2);
            max-width: 800px;
        }
        
        .sdg-badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.9);
            color: #1A1A2E;
            padding: 8px 20px;
            border-radius: 50px;
            margin: 5px;
            font-weight: bold;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            border: 2px solid #4ECDC4;
        }
        
        .hot-button {
            background: linear-gradient(45deg, #FF6B6B, #FFD93D);
            color: #1A1A2E;
            padding: 18px 45px;
            border-radius: 50px;
            border: none;
            font-size: 1.4rem;
            font-weight: 800;
            cursor: pointer;
            margin-top: 30px;
            box-shadow: 0 10px 30px rgba(255, 107, 107, 0.4);
            transition: all 0.3s ease;
            display: inline-block;
            text-decoration: none;
        }
        
        .hot-button:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 15px 40px rgba(255, 107, 107, 0.6);
        }
        </style>

        <div class="welcome-container">
            <h1>🧠 MindMate</h1>
            <h3>Your AI-Powered Mental Wellness Companion</h3>
            <p>
                Welcome to the <b>future of mental health support</b> — where technology meets empathy. 
                MindMate is designed to be your <b>24/7 companion</b> for emotional wellness, stress management, 
                and personal growth. We combine <b>evidence-based techniques</b> with <b>cutting-edge AI</b> 
                to create personalized mental health journeys.
            </p>
            
            <div class="welcome-points">
                💖 <b>Real-time Mood Tracking</b> with smart insights<br>
                🌱 <b>Personalized Coping Strategies</b> that actually work<br>
                🤖 <b>AI-Powered Support</b> available anytime, anywhere<br>
                🌍 <b>Global SDG Alignment</b> contributing to better mental health for all<br>
                🎮 <b>Therapeutic Games</b> for skill building through play<br>
                👥 <b>Community Connection</b> with safe, moderated spaces
            </div>
            
            <div style="margin: 30px 0;">
                <h4 style="color: #1A1A2E; margin-bottom: 15px;">🌍 Supporting UN Sustainable Development Goals:</h4>
                <div class="sdg-badge">SDG 3: Good Health & Well-being</div>
                <div class="sdg-badge">SDG 4: Quality Education</div>
                <div class="sdg-badge">SDG 10: Reduced Inequalities</div>
                <div class="sdg-badge">SDG 17: Partnerships for Goals</div>
            </div>
            
            <a class="hot-button" href="#">🚀 Begin Your Wellness Journey</a>
        </div>
    """, unsafe_allow_html=True)

def mental_health_assessment_page():
    st.markdown("""
        <style>
        .assessment-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px;
            padding: 30px;
            margin: 20px 0;
            color: white;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            border: 2px solid rgba(255,255,255,0.1);
        }
        
        .slider-container {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            margin: 15px 0;
        }
        
        .stSlider > div > div > div {
            background: linear-gradient(90deg, #FF6B6B, #FFD93D, #4ECDC4);
        }
        
        .result-card {
            background: rgba(255,255,255,0.95);
            border-radius: 20px;
            padding: 25px;
            margin: 20px 0;
            border-left: 8px solid;
            animation: slideIn 0.5s ease-out;
        }
        
        @keyframes slideIn {
            from {opacity: 0; transform: translateY(20px);}
            to {opacity: 1; transform: translateY(0);}
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🧠 Mental Health Assessment")
    st.markdown("### 🌈 Let's check in with how you're feeling today")
    
    with st.container():
        st.markdown('<div class="assessment-card">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("😊 Current Mood")
            mood_score = st.slider("How's your overall mood today?", 0, 100, 50, 
                                  help="0 = Very low, 100 = Excellent")
            
            if mood_score < 30:
                mood_emoji = "😔"
                mood_text = "Having a tough time"
            elif mood_score < 70:
                mood_emoji = "😌"
                mood_text = "Managing okay"
            else:
                mood_emoji = "🌟"
                mood_text = "Feeling great!"
            
            st.markdown(f"### {mood_emoji} {mood_text}")
        
        with col2:
            st.subheader("😰 Stress Level")
            stress_score = st.slider("How stressed do you feel?", 0, 100, 30,
                                    help="0 = Completely calm, 100 = Overwhelmed")
            
            if stress_score < 30:
                stress_emoji = "😊"
                stress_text = "Very calm"
            elif stress_score < 70:
                stress_emoji = "😟"
                stress_text = "Moderate stress"
            else:
                stress_emoji = "😰"
                stress_text = "Very stressed"
            
            st.markdown(f"### {stress_emoji} {stress_text}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional factors
    with st.expander("📝 Additional Factors (Optional)"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            sleep = st.slider("💤 Sleep quality", 0, 100, 70)
        with col2:
            energy = st.slider("⚡ Energy level", 0, 100, 60)
        with col3:
            focus = st.slider("🎯 Focus & concentration", 0, 100, 65)
    
    if st.button("🔍 Get Personalized Recommendations", use_container_width=True):
        mood_level = classify(mood_score)
        stress_level = classify(stress_score)
        
        st.markdown("## 🎯 Your Personalized Wellness Plan")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="result-card" style="border-left-color: #4ECDC4;">', unsafe_allow_html=True)
            st.subheader("💖 Mood Support")
            st.markdown(mental_health_assessment["mood"][mood_level])
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="result-card" style="border-left-color: #FF6B6B;">', unsafe_allow_html=True)
            st.subheader("🛡️ Stress Management")
            st.markdown(mental_health_assessment["stress"][stress_level])
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Visualization
        st.plotly_chart(create_mood_chart(), use_container_width=True)

def sdg_page():
    st.markdown("""
        <style>
        .sdg-header {
            background: linear-gradient(135deg, #1A1A2E 0%, #16213E 100%);
            padding: 40px;
            border-radius: 25px;
            color: white;
            margin-bottom: 30px;
            text-align: center;
            border: 3px solid #4ECDC4;
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        }
        
        .sdg-card {
            background: white;
            border-radius: 20px;
            padding: 25px;
            margin: 20px 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            border-top: 8px solid;
            transition: transform 0.3s ease;
        }
        
        .sdg-card:hover {
            transform: translateY(-10px);
        }
        
        .impact-metric {
            background: linear-gradient(45deg, #FF6B6B, #FFD93D);
            color: white;
            padding: 15px;
            border-radius: 15px;
            text-align: center;
            font-weight: bold;
            margin: 10px;
            box-shadow: 0 5px 15px rgba(255,107,107,0.3);
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="sdg-header">', unsafe_allow_html=True)
    st.title("🌍 UN Sustainable Development Goals")
    st.markdown("### How MindMate Contributes to Global Mental Health Targets")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # SDG Cards - FIXED THIS SECTION
    for sdg_num, info in SDG_INFO.items():
        with st.container():
            color = info["color"]
            icon = info["icon"]
            title = info["title"]
            description = info["description"]
            
            st.markdown(f'<div class="sdg-card" style="border-top-color: {color};">', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 3])
            
            with col1:
                st.markdown(f'<h1 style="font-size: 4rem; color: {color};">{icon}</h1>', unsafe_allow_html=True)
                st.markdown(f'<h3 style="color: {color};">SDG {sdg_num}</h3>', unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"### {title}")
                st.markdown(f"*{description}*")
                
                st.markdown("**How MindMate contributes:**")
                for target in info["targets"]:
                    st.markdown(f"- ✅ {target}")
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Impact Metrics
    st.markdown("## 📊 Our Global Impact")
    
    cols = st.columns(4)
    metrics = [
        ("Users Supported", "10,000+", "👥"),
        ("Countries Reached", "50+", "🌎"),
        ("Daily Check-ins", "5,000+", "📱"),
        ("Crisis Interventions", "500+", "🆘")
    ]
    
    for idx, (title, value, icon) in enumerate(metrics):
        with cols[idx]:
            st.markdown(f'<div class="impact-metric">', unsafe_allow_html=True)
            st.markdown(f"<h3>{icon} {value}</h3>", unsafe_allow_html=True)
            st.markdown(f"<small>{title}</small>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Partnership Section
    st.markdown("## 🤝 Global Partnerships")
    st.markdown("""
    We collaborate with organizations worldwide to advance mental health:
    
    - **WHO Mental Health Atlas** - Data sharing and research
    - **Local NGOs** - Cultural adaptation of resources
    - **Educational Institutions** - Youth mental health programs
    - **Tech Companies** - AI ethics and accessibility
    """)

def therapeutic_games():
    st.markdown("""
        <style>
        .game-card {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            border-radius: 25px;
            padding: 25px;
            margin: 15px 0;
            color: white;
            text-align: center;
            transition: all 0.3s ease;
            border: 3px solid rgba(255,255,255,0.2);
            cursor: pointer;
        }
        
        .game-card:hover {
            transform: scale(1.03);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        }
        
        .game-icon {
            font-size: 4rem;
            margin-bottom: 15px;
        }
        
        .breathing-circle {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            margin: 20px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            font-weight: bold;
            color: white;
            animation: pulse 4s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); background: #FF6B6B; }
            50% { transform: scale(1.1); background: #4ECDC4; }
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🎮 Therapeutic Games")
    st.markdown("### Play your way to better mental health")
    
    # Games selection
    games = [
        {"emoji": "🌀", "name": "Breathing Exercises", "desc": "Calm your nervous system"},
        {"emoji": "🧩", "name": "Mindfulness Puzzles", "desc": "Focus and present moment awareness"},
        {"emoji": "🎨", "name": "Creative Expression", "desc": "Art therapy techniques"},
        {"emoji": "📝", "name": "Gratitude Journal", "desc": "Positive psychology practice"},
        {"emoji": "🎵", "name": "Music Therapy", "desc": "Sound healing and mood regulation"},
        {"emoji": "🌿", "name": "Nature Connection", "desc": "Virtual forest bathing"}
    ]
    
    cols = st.columns(3)
    for idx, game in enumerate(games):
        with cols[idx % 3]:
            emoji = game["emoji"]
            name = game["name"]
            desc = game["desc"]
            
            st.markdown(f'''
                <div class="game-card">
                    <div class="game-icon">{emoji}</div>
                    <h3>{name}</h3>
                    <p>{desc}</p>
                </div>
            ''', unsafe_allow_html=True)
    
    # Breathing Exercise Game
    st.markdown("## 🌬️ Interactive Breathing Exercise")
    
    if "breathing_phase" not in st.session_state:
        st.session_state.breathing_phase = "inhale"
        st.session_state.breathing_time = 4
    
    col1, col2, col3 = st.columns([2, 3, 2])
    
    with col2:
        phase_display = {
            "inhale": {"text": "INHALE", "color": "#4ECDC4", "instruction": "Breathe in slowly..."},
            "hold": {"text": "HOLD", "color": "#FFD93D", "instruction": "Hold gently..."},
            "exhale": {"text": "EXHALE", "color": "#FF6B6B", "instruction": "Release slowly..."}
        }
        
        current = phase_display[st.session_state.breathing_phase]
        current_color = current["color"]
        current_text = current["text"]
        instruction_text = current["instruction"]
        breathing_time = st.session_state.breathing_time
        
        st.markdown(f'''
            <div class="breathing-circle" style="background: {current_color};">
                {current_text}<br>
                {breathing_time}s
            </div>
        ''', unsafe_allow_html=True)
        
        st.markdown(f"### {instruction_text}")
    
    if st.button("▶️ Start Exercise", use_container_width=True):
        st.session_state.breathing_phase = "inhale"
        st.session_state.breathing_time = 4
        st.success("Focus on your breath... Let's begin!")
    
    # Quick meditation timer
    st.markdown("## 🧘 Quick Meditation Timer")
    meditation_time = st.slider("Select meditation duration (minutes)", 1, 30, 5)
    
    if st.button(f"⏱️ Start {meditation_time} Minute Meditation", use_container_width=True):
        with st.spinner(f"Meditating for {meditation_time} minutes... Find a comfortable position"):
            time.sleep(2)
            st.success("Meditation complete! Notice how you feel.")

def community_page():
    st.markdown("""
        <style>
        .community-card {
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            border-radius: 25px;
            padding: 30px;
            margin: 20px 0;
            color: #1A1A2E;
        }
        
        .user-post {
            background: white;
            border-radius: 20px;
            padding: 20px;
            margin: 15px 0;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            border-left: 5px solid #4ECDC4;
        }
        
        .support-group {
            background: rgba(255,255,255,0.9);
            border-radius: 20px;
            padding: 20px;
            margin: 10px 0;
            border: 2px solid #FF6B6B;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("👥 MindMate Community")
    st.markdown("### Connect, share, and grow together")
    
    # Safe space guidelines
    with st.expander("🏳️‍🌈 Community Guidelines (Read First)"):
        st.markdown("""
        **Our community is built on:**
        
        ✅ **Confidentiality** - What's shared here stays here
        ✅ **Respect** - All experiences and identities are valid
        ✅ **Compassion** - Lead with kindness and understanding
        ✅ **Support, Not Advice** - Share what worked for you, not prescriptions
        ✅ **No Judgement** - This is a safe space for vulnerability
        
        🚫 **Zero Tolerance For:** Harassment, discrimination, medical advice, or promotion
        """)
    
    # Support Groups
    st.markdown("## 🤗 Support Groups")
    
    groups = [
        {"name": "Anxiety & Stress", "members": "1.2k", "emoji": "😰", "schedule": "Daily check-ins"},
        {"name": "Depression Support", "members": "890", "emoji": "😔", "schedule": "Mon/Wed/Fri"},
        {"name": "Mindfulness Practice", "members": "2.3k", "emoji": "🧘", "schedule": "Daily 8 AM & 8 PM"},
        {"name": "LGBTQ+ Mental Health", "members": "1.5k", "emoji": "🏳️‍🌈", "schedule": "24/7 moderated"},
        {"name": "Students & Youth", "members": "3.1k", "emoji": "🎓", "schedule": "Evening sessions"},
        {"name": "Parents & Caregivers", "members": "1.8k", "emoji": "👨‍👩‍👧‍👦", "schedule": "Weekend circles"}
    ]
    
    cols = st.columns(3)
    for idx, group in enumerate(groups):
        with cols[idx % 3]:
            group_name = group["name"]
            group_emoji = group["emoji"]
            group_members = group["members"]
            group_schedule = group["schedule"]
            
            st.markdown(f'''
                <div class="support-group">
                    <h3>{group_emoji} {group_name}</h3>
                    <p>👥 {group_members} members</p>
                    <p>⏰ {group_schedule}</p>
                </div>
            ''', unsafe_allow_html=True)
    
    # Community Posts
    st.markdown("## 💬 Recent Community Posts")
    
    posts = [
        {"user": "Alex 🌈", "text": "Today I managed my anxiety enough to attend class. Small win!", "likes": "42", "time": "2h ago"},
        {"user": "Sam 🎨", "text": "Started gratitude journaling and it's slowly changing my perspective", "likes": "28", "time": "5h ago"},
        {"user": "Jordan 🏃‍♂️", "text": "Did 10 minutes of breathing exercises instead of panic scrolling", "likes": "56", "time": "1d ago"},
        {"user": "Taylor 🌿", "text": "First therapy session today - proud of myself for taking this step", "likes": "89", "time": "2d ago"}
    ]
    
    for post in posts:
        with st.container():
            post_user = post["user"]
            post_text = post["text"]
            post_time = post["time"]
            post_likes = post["likes"]
            
            st.markdown(f'''
                <div class="user-post">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4>{post_user}</h4>
                        <small>{post_time}</small>
                    </div>
                    <p>{post_text}</p>
                    <div style="color: #FF6B6B;">❤️ {post_likes} hearts</div>
                </div>
            ''', unsafe_allow_html=True)
    
    # Create new post
    st.markdown("## 📝 Share Your Journey")
    
    with st.form("new_post"):
        post_content = st.text_area("Share your experience, win, or reflection", 
                                   placeholder="Today I'm grateful for...", 
                                   height=100)
        
        col1, col2 = st.columns(2)
        with col1:
            anonymous = st.checkbox("Post anonymously")
        with col2:
            trigger_warning = st.checkbox("Add content warning")
        
        if st.form_submit_button("✨ Share with Community"):
            if post_content:
                st.success("Post shared! Our community welcomes you 🤗")
            else:
                st.warning("Please share something to post")

def crisis_support_page():
    st.markdown("""
        <style>
        .emergency-card {
            background: linear-gradient(135deg, #FF6B6B, #FF8E8E);
            color: white;
            padding: 30px;
            border-radius: 25px;
            text-align: center;
            margin: 20px 0;
            border: 3px solid #FFD93D;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% {box-shadow: 0 0 20px rgba(255,107,107,0.5);}
            50% {box-shadow: 0 0 40px rgba(255,107,107,0.8);}
        }
        
        .resource-card {
            background: white;
            border-radius: 20px;
            padding: 25px;
            margin: 15px 0;
            border-left: 8px solid #4ECDC4;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .country-flag {
            font-size: 2rem;
            margin-right: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="emergency-card">', unsafe_allow_html=True)
    st.title("🆘 Crisis & Immediate Support")
    st.markdown("### **You are not alone. Help is available right now.**")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Immediate Help Section
    st.markdown("## 📞 Immediate Help Lines")
    
    emergency_lines = [
        {"country": "🇺🇸 USA", "numbers": ["988 (Suicide & Crisis Lifeline)", "1-800-273-TALK (8255)"], "text": "Text HOME to 741741"},
        {"country": "🇬🇧 UK", "numbers": ["116 123 (Samaritans)", "999 (Emergency)"], "text": "Text SHOUT to 85258"},
        {"country": "🇮🇳 India", "numbers": ["9152987821 (iCall)", "044-24640050"], "text": "Available 10AM-8PM"},
        {"country": "🇨🇦 Canada", "numbers": ["1-833-456-4566", "911 (Emergency)"], "text": "Text 45645"},
        {"country": "🇦🇺 Australia", "numbers": ["13 11 14", "000 (Emergency)"], "text": "Text 0477 13 11 14"},
        {"country": "🌍 International", "numbers": ["Find your country's line"], "text": "befrienders.org"}
    ]
    
    for line in emergency_lines:
        with st.container():
            country = line["country"]
            numbers = line["numbers"]
            text_line = line["text"]
            
            numbers_html = '<br>'.join(f"📞 {num}" for num in numbers)
            
            st.markdown(f'''
                <div class="resource-card">
                    <h3>{country}</h3>
                    <div style="margin: 15px 0;">
                        <strong>Phone:</strong><br>
                        {numbers_html}
                    </div>
                    <div style="color: #FF6B6B;">
                        <strong>Text:</strong> {text_line}
                    </div>
                </div>
            ''', unsafe_allow_html=True)
    
    # Grounding Techniques
    st.markdown("## 🌈 Grounding Techniques (Right Now)")
    
    techniques = [
        {"name": "5-4-3-2-1 Method", "steps": [
            "Look for 5 things you can SEE",
            "Touch 4 things you can FEEL",
            "Listen for 3 things you can HEAR",
            "Notice 2 things you can SMELL",
            "Find 1 thing you can TASTE"
        ]},
        {"name": "Temperature Shock", "steps": [
            "Hold an ice cube for 30 seconds",
            "Splash cold water on your face",
            "Hold a warm beverage in both hands"
        ]},
        {"name": "Breathing Anchor", "steps": [
            "Place hand on chest",
            "Breathe in for 4 counts",
            "Hold for 4 counts",
            "Breathe out for 6 counts",
            "Repeat 5 times"
        ]}
    ]
    
    cols = st.columns(3)
    for idx, tech in enumerate(techniques):
        with cols[idx]:
            tech_name = tech["name"]
            steps = tech["steps"]
            
            with st.expander(f"✨ {tech_name}", expanded=True):
                for step in steps:
                    st.markdown(f"• {step}")
    
    # Safety Plan Builder
    st.markdown("## 🛡️ Create Your Safety Plan")
    
    with st.form("safety_plan"):
        st.markdown("**Step 1: Warning Signs**")
        signs = st.text_area("What are your early warning signs?", 
                           placeholder="e.g., trouble sleeping, irritability, isolation...")
        
        st.markdown("**Step 2: Coping Strategies**")
        strategies = st.text_area("What helps when you notice these signs?", 
                                placeholder="e.g., call a friend, go for a walk, breathing exercises...")
        
        st.markdown("**Step 3: People to Contact**")
        contacts = st.text_area("Who can you reach out to? (Name & Number)", 
                              placeholder="e.g., Sarah: 555-0123, Therapist: 555-4567...")
        
        st.markdown("**Step 4: Professional Resources**")
        professionals = st.text_area("Professional contacts and crisis lines", 
                                   placeholder="e.g., Crisis line: 988, Therapist: Dr. Smith...")
        
        if st.form_submit_button("💾 Save Safety Plan"):
            st.success("Safety plan saved! Consider printing this and keeping it accessible.")
            st.download_button(
                label="📥 Download Safety Plan",
                data=f"""
                MINDMATE SAFETY PLAN
                ====================
                
                Warning Signs:
                {signs}
                
                Coping Strategies:
                {strategies}
                
                People to Contact:
                {contacts}
                
                Professional Resources:
                {professionals}
                
                Created: {datetime.datetime.now().strftime("%Y-%m-%d")}
                """,
                file_name="mindmate_safety_plan.txt"
            )

def main():
    st.set_page_config(
        page_title="MindMate - Mental Wellness Companion",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for hot design
    st.markdown("""
        <style>
        /* Main theme */
        .main {
            background: linear-gradient(135deg, #1A1A2E 0%, #16213E 100%);
            color: white;
        }
        
        /* Sidebar styling */
        .css-1d391kg, .css-12oz5g7 {
            background: linear-gradient(180deg, #0F3460 0%, #1A1A2E 100%);
        }
        
        /* Hot buttons */
        .stButton > button {
            background: linear-gradient(45deg, #FF6B6B, #FFD93D);
            color: #1A1A2E;
            border: none;
            padding: 12px 24px;
            border-radius: 25px;
            font-weight: 800;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 25px rgba(255,107,107,0.4);
        }
        
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: rgba(255,255,255,0.1);
            border-radius: 15px 15px 0 0;
            padding: 10px 20px;
            color: white;
            border: 2px solid rgba(255,255,255,0.2);
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(45deg, #FF6B6B, #FFD93D);
            color: #1A1A2E !important;
            font-weight: bold;
        }
        
        /* Logo in sidebar */
        .sidebar-logo {
            text-align: center;
            margin-bottom: 30px;
        }
        
        .sidebar-logo h1 {
            font-size: 2.5rem;
            background: linear-gradient(45deg, #FF6B6B, #FFD93D, #4ECDC4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
        }
        
        /* Stats in sidebar */
        .sidebar-stats {
            background: rgba(255,255,255,0.1);
            padding: 15px;
            border-radius: 15px;
            margin: 15px 0;
            border: 2px solid rgba(255,255,255,0.2);
        }
        
        /* Floating particles */
        @keyframes float {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }
        
        .floating-emoji {
            position: fixed;
            font-size: 2rem;
            animation: float 5s infinite ease-in-out;
            z-index: -1;
        }
        </style>
        
        <!-- Floating emojis for background -->
        <div class="floating-emoji" style="top: 10%; left: 5%;">🧠</div>
        <div class="floating-emoji" style="top: 20%; right: 10%; animation-delay: -1s;">💖</div>
        <div class="floating-emoji" style="top: 60%; left: 15%; animation-delay: -2s;">🌱</div>
        <div class="floating-emoji" style="top: 40%; right: 5%; animation-delay: -3s;">✨</div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("""
            <div class="sidebar-logo">
                <h1>🧠 MindMate</h1>
                <p>Your Mental Wellness Companion</p>
            </div>
        """, unsafe_allow_html=True)
        
        # User stats
        st.markdown("""
            <div class="sidebar-stats">
                <h3>📊 Your Stats</h3>
                <p>🔄 14-day streak</p>
                <p>😊 Avg mood: 7.2/10</p>
                <p>🎮 8 games completed</p>
                <p>📝 12 journal entries</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Quick actions
        st.markdown("### ⚡ Quick Actions")
        if st.button("🎯 Daily Check-in", use_container_width=True):
            st.session_state.active_tab = "Assessment"
        
        if st.button("🌬️ Breathing Exercise", use_container_width=True):
            st.session_state.active_tab = "Therapeutic Games"
        
        if st.button("🆘 Crisis Support", use_container_width=True):
            st.session_state.active_tab = "Crisis Support"
        
        if st.button("📝 Quick Journal", use_container_width=True):
            st.session_state.active_tab = "Community"
        
        # Emergency contact
        st.markdown("---")
        st.markdown("### 🚨 Emergency")
        st.info("Need immediate help?")
        if st.button("📞 Show Crisis Lines", use_container_width=True):
            st.session_state.active_tab = "Crisis Support"
    
    # Main content with tabs
    tabs = st.tabs([
        "🏠 Welcome", 
        "🧠 Assessment", 
        "🎮 Therapeutic Games", 
        "👥 Community", 
        "🌍 SDG Impact",
        "🆘 Crisis Support"
    ])
    
    with tabs[0]:
        welcome_page()
    
    with tabs[1]:
        mental_health_assessment_page()
    
    with tabs[2]:
        therapeutic_games()
    
    with tabs[3]:
        community_page()
    
    with tabs[4]:
        sdg_page()
    
    with tabs[5]:
        crisis_support_page()

if __name__ == "__main__":
    main()