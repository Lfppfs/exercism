def find_anagrams(word, candidates):
    word = word.lower()
    word_aux = sorted(word)

    words_to_remove = []
    for candidate in candidates:
        if candidate.lower() == word:
            words_to_remove.append(candidate)
        candidate_aux = candidate.lower()
        candidate_aux = sorted(candidate_aux)

        if len(candidate_aux) != len(word_aux):
            words_to_remove.append(candidate)
            continue

        for i, j in zip(word_aux, candidate_aux):
            if i != j:
                words_to_remove.append(candidate)
                break

    for i in words_to_remove:
        candidates.remove(i)

    return candidates