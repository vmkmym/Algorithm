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

# 다른 사람의 풀이
def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)

    while len(dic) > 0:
        play_genre = dic.pop(0)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play