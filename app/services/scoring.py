from . import firestore_client

global total_score
total_score = 0

def record_answer(question_id, score_value):
    """
    Receives an answer and updates the statistics for that question in Firestore.
    
    Args:
        question_id (str or int): The identifier for the question.
        score_value (int or float): The score of the answer.
    """
    if not isinstance(score_value, (int, float)):
        print("Error: score_value must be a number.")
        return
        
    # Call the firestore_client function to update the statistics.
    firestore_client.update_question_stats(question_id, score_value)

    total_score += score_value

def get_total_score():
    return total_score