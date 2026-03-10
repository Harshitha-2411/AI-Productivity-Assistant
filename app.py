import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

from tasks import add_task, get_tasks, complete_task, delete_task
from ai_engine import get_intent, chat_with_ai

st.set_page_config(page_title="AI Productivity Assistant", layout="wide")

st.title("AI Productivity Assistant")

# ---------------- DASHBOARD ----------------

tasks = get_tasks()

total = len(tasks)
pending = len([t for t in tasks if t[2] == "pending"])
completed = len([t for t in tasks if t[2] == "completed"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Tasks", total)
col2.metric("Pending Tasks", pending)
col3.metric("Completed Tasks", completed)

# -------- PIE CHART --------

if total > 0:

    labels = ["Pending","Completed"]
    values = [pending,completed]

    fig, ax = plt.subplots()

    ax.pie(values, labels=labels, autopct="%1.0f%%")
    ax.set_title("Task Status")

    st.pyplot(fig)

st.divider()

# --------------- TASK TABLE ----------------

st.subheader("Task List")

if tasks:

    df = pd.DataFrame(tasks, columns=["ID","Task","Status"])

    st.dataframe(df)

else:

    st.write("No tasks available")

st.divider()

# ---------------- AI ASSISTANT ----------------

st.subheader("AI Assistant")

user_input = st.text_input("Type your command")

if st.button("Send"):

    intent = get_intent(user_input)

    # ADD TASK
    if intent == "add_task":

        task = user_input.replace("add task","").strip()

        add_task(task)

        st.success("Task added")

    # SHOW TASKS
    elif intent == "show_tasks":

        tasks = get_tasks()

        for t in tasks:
            st.write(f"ID:{t[0]} | {t[1]} | {t[2]}")

    # COMPLETE TASK
    elif intent == "complete_task":

        number = re.findall(r'\d+', user_input)

        if number:

            task_id = int(number[0])

            complete_task(task_id)

            st.success(f"Task {task_id} completed")

        else:

            st.warning("Please specify task number")

    # DELETE TASK
    elif intent == "delete_task":

        number = re.findall(r'\d+', user_input)

        if number:

            task_id = int(number[0])

            delete_task(task_id)

            st.success(f"Task {task_id} deleted")

        else:

            st.warning("Please specify task number")

    # PLAN DAY
    elif intent == "plan_day":

        tasks = get_tasks()

        task_list = [t[1] for t in tasks]

        prompt = f"Plan a productive day using these tasks: {task_list}"

        plan = chat_with_ai(prompt)

        st.write(plan)

    # CHAT
    else:

        reply = chat_with_ai(user_input)

        st.write(reply)