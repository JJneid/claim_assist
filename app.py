import streamlit as st
import random
from datetime import datetime

# Simulated database of policies and clauses
policies = {
    "P001": {
        "name": "Jneid Jneid",
        "policy_type": "Auto Insurance",
        "coverage": ["Collision", "Comprehensive", "Liability"],
    },
    "P002": {
        "name": "Jane Smith",
        "policy_type": "Home Insurance",
        "coverage": ["Property Damage", "Liability", "Natural Disasters"],
    }
}

underwriting_clauses = {
    "Auto Insurance": {
        "Collision": "Covers damage to your vehicle in a collision with another vehicle or object.",
        "Comprehensive": "Covers damage to your vehicle from non-collision events like theft, vandalism, or natural disasters.",
        "Liability": "Covers bodily injury and property damage you cause to others in an auto accident."
    },
    "Home Insurance": {
        "Property Damage": "Covers damage to your home and personal property.",
        "Liability": "Covers legal and medical expenses if someone is injured on your property.",
        "Natural Disasters": "Covers damage from specific natural events like hurricanes or earthquakes."
    }
}

def get_policy_info(policy_id):
    return policies.get(policy_id, None)

def check_coverage(policy_id, claim_type):
    policy = get_policy_info(policy_id)
    if policy and claim_type in policy['coverage']:
        return True, underwriting_clauses[policy['policy_type']][claim_type]
    return False, "Not covered"

def main():
    st.title("Business Assistant Interface")

    # Sidebar for call information
    st.sidebar.header("Call Information")
    caller_id = st.sidebar.text_input("Caller ID", value="P001")
    call_duration = st.sidebar.metric("Call Duration", value="00:00")

    # Main interface
    col1, col2 = st.columns(2)

    with col1:
        st.header("Policy Information")
        policy = get_policy_info(caller_id)
        if policy:
            st.write(f"Name: {policy['name']}")
            st.write(f"Policy Type: {policy['policy_type']}")
            st.write("Coverage:")
            for item in policy['coverage']:
                st.write(f"- {item}")
        else:
            st.write("No policy found for this ID")

    with col2:
        st.header("AI Assistant")
        user_input = st.text_input("Ask a question about the policy:","is the client covered for an accident claim?")
        if st.button("Submit"):
            if "accident claim" in user_input.lower():
                claim_type = random.choice(policy['coverage'])  # Randomly select a coverage type for this example
                is_covered, clause = check_coverage(caller_id, claim_type)
                if is_covered:
                    st.success(f"The client is covered for {claim_type}.")
                    st.info(f"Relevant clause: {clause}")
                else:
                    st.error(f"The client is not covered for {claim_type}.")
            else:
                st.write("I'm sorry, I don't understand the question. Please ask about a specific accident claim.")

    # Underwriting Clauses
    st.header("Underwriting Clauses")
    if policy:
        for coverage, clause in underwriting_clauses[policy['policy_type']].items():
            with st.expander(coverage):
                st.write(clause)

    # Call Summary
    st.header("Call Summary")
    if st.button("End Call and Generate Summary"):
        st.write("Call ended at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        st.write("Summary: Discussed policy coverage for accident claim.")
        st.write("Follow-up: Send detailed policy information via email.")

if __name__ == "__main__":
    main()