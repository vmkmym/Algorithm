def solution(genres, plays):
    genre_dict = {} # {장르, [(재생횟수, 고유번호)]}
    play_dict = {} # 장르별 총 재생횟수 {장르, 재생횟수}

    for i in range(len(genres)):
        if genres[i] not in play_dict:
            play_dict[genres[i]] = plays[i]
            genre_dict[genres[i]] = [(plays[i], i)]
        else:
            play_dict[genres[i]] += plays[i]
            genre_dict[genres[i]].append((plays[i], i))

    sorted_genres = sorted(play_dict.items(), key=lambda x: x[1], reverse=True) # 재생횟수 내림차순 정렬
    
    best_album = []
    for genre in sorted_genres:
        sorted_genre = sorted(genre_dict[genre[0]], key=lambda x: (-x[0], x[1])) # 재생횟수 내림차순, 고유번호 오름차순 정렬
        best_album.extend([song[1] for song in sorted_genre[:2]])
    return best_album