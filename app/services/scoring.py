from . import firestore_client

def record_answer(question_id, score_value):
    """
    Receives an answer and updates the statistics for that question in Firestore.
    """
    if not isinstance(score_value, (int, float)):
        print("Error: score_value must be a number.")
        return
        
    # Call the firestore_client function to update the statistics.
    firestore_client.update_question_stats(question_id, score_value)

