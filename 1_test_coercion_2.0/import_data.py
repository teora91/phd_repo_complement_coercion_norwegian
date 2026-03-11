from utils import *


def import_data():
    list_lemma_inflected = pd.read_csv("data_for_task/list_lemma_coercion_inflected_updated_02-12-24.csv")

    with open("data_for_task/entity_verb_association_updated_02-12-24.json", "r") as file:
        entity_verb_association_NCC = json.load(file)

    return list_lemma_inflected, entity_verb_association_NCC
