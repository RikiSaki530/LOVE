import os
import firebase_admin
from firebase_admin import credentials, firestore

# --- Firestore Initialization ---
# Get the absolute path to the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
# Construct the path to the service account key, assuming it's in the project root
key_path = os.path.join(project_root , 'serviceAccountKey.json')

try:
    # Prevent re-initialization error
    if not firebase_admin._apps:
        cred = credentials.Certificate(key_path)
        firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("Firestore client initialized successfully.")
except Exception as e:
    print(f"Error initializing Firestore client: {e}")
    db = None


def update_question_stats(question_id, new_score):
    """
    Atomically updates the statistics for a given question:
    - avgScore
    - responseCount
    - updatedAt
    """
    if not db:
        print("Firestore client is not initialized. Cannot update stats.")
        return

    doc_ref = db.collection('question_stats').document(str(question_id))

    try:
        @firestore.transactional
        def update_in_transaction(transaction, doc_ref, new_score):
            """
            Safely reads, calculates, and writes the new stats within a transaction.
            """
            snapshot = doc_ref.get(transaction=transaction)

            if not snapshot.exists:
                # First response for this question
                new_avg = float(new_score)
                new_count = 1
            else:
                # Calculate new average
                data = snapshot.to_dict()
                current_avg = data.get('avgScore', 0)
                current_count = data.get('responseCount', 0)

                new_count = current_count + 1
                new_avg = ((current_avg * current_count) + new_score) / new_count

            # Set the new data in the transaction
            transaction.set(doc_ref, {
                'avgScore': new_avg,
                'responseCount': new_count,
                'updatedAt': firestore.SERVER_TIMESTAMP,
            })

        # Execute the transaction
        update_in_transaction(db.transaction(), doc_ref, new_score)
        print(f"Stats updated for question_id: {question_id}")

    except Exception as e:
        print(f"An error occurred while updating stats: {e}")


def get_question_stats(question_id):
    """
    Retrieves the statistics for a specific question.
    Returns a dict with avgScore, responseCount, and updatedAt, or None if not found.
    """
    if not db:
        print("Firestore client is not initialized. Cannot get stats.")
        return None

    try:
        doc_ref = db.collection('question_stats').document(str(question_id))
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            print(f"No stats found for question_id: {question_id}")
            return None

    except Exception as e:
        print(f"An error occurred while getting stats: {e}")
        return None