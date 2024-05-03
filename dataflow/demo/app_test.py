from google.cloud import pubsub_v1
import json

def publish_message(project_id, topic_name, message):
    # Crea un cliente de Pub/Sub
    publisher = pubsub_v1.PublisherClient()

    # Formatea el nombre completo del tema
    topic_path = publisher.topic_path(project_id, topic_name)

    # Convierte el mensaje a formato JSON
    message_json = json.dumps(message).encode('utf-8')

    # Publica el mensaje en el tema
    future = publisher.publish(topic_path, data=message_json)
    message_id = future.result()

    print(f"Mensaje publicado en el tema {topic_name}. ID del mensaje: {message_id}")

# Ejemplo de uso
if __name__ == "__main__":
    project_id = "premium-guide-410714"
    topic_name = "topic_card"
    message = {
        "name":"Luis",
        "email":"luis.prueba@prueba.com",
        "document":"9899999",
        "comments":"Test",
        "card":"4444444",
        "created_datetime":"2024-05-03"
    }

    publish_message(project_id, topic_name, message)
