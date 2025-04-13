import streamlit as st
import time

st.set_page_config(page_title="Dark Web Simulator", page_icon="🕵️")

st.title("🕵️ Dark Web Simulator (Educational)")
st.caption("Explore a simulated darknet safely. Learn how it works — without risk.")

st.markdown("💻 **Terminal:** Type your commands below to explore.")
st.info("Try commands like: `connect darknet`, `visit hidden wiki`, `open marketplace`, `search bitcoin`, `exit`")

# Initialize session state for terminal history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input(">>>", key="input")

# Response logic
def process_command(cmd):
    cmd = cmd.lower().strip()
    if cmd == "connect darknet":
        return "🔐 Connecting via Tor network...\n🧅 Onion routing initialized across 3 relays."
    elif cmd == "visit hidden wiki":
        return "📚 Loaded: Hidden Wiki - A list of .onion sites (simulated)\n- Marketplace\n- Forums\n- Whistleblowing portals"
    elif cmd == "open marketplace":
        return "🛒 You entered a fake market: 'Silkplace v2'\nListings: Fake IDs, Credit Cards, Malware Toolkits\n⚠️ Reminder: This is just a simulation!"
    elif cmd == "search bitcoin":
        return "💰 Searching...\nBitcoin address generator loaded. Fake balance: 0.892 BTC (⚠️ for demo only)"
    elif cmd == "exit":
        return "Session ended. You safely disconnected from the darknet simulation. 🛡️"
    else:
        return "🤖 Unknown command. Type `connect darknet` to begin."

# Handle user input
if user_input:
    response = process_command(user_input)
    st.session_state.history.append((user_input, response))
    st.experimental_rerun()

# Display terminal history
for cmd, res in st.session_state.history:
    st.markdown(f"**>>> {cmd}**")
    st.code(res)
