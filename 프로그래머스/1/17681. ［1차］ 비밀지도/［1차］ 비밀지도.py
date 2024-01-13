def solution(n, arr1, arr2):
    result = []

    for r1, r2 in zip(arr1, arr2):
        binary = bin(r1 | r2)[2:].zfill(n)
        row = ''.join(['#' if bit == '1' else ' ' for bit in binary])
        result.append(row)
    
    return result

# 줄이기
def solution(n, arr1, arr2):
    return [''.join(['#' if bit == '1' else ' ' for bit in bin(r1 | r2)[2:].zfill(n)]) for r1, r2 in zip(arr1, arr2)]

#  `rjust`와 `zfill`은 각각 문자열의 길이를 맞추기 위해 사용되는 메서드입니다.

1. **`rjust(width[, fillchar])`**:
   - 문자열의 오른쪽에 지정된 길이만큼의 공백이나 다른 문자를 추가하여 문자열의 폭(길이)을 맞춥니다.
   - `width`: 최종 문자열의 폭(길이)을 나타내는 정수값.
   - `fillchar` (선택 사항): 문자열의 길이를 맞추기 위해 사용되는 채워넣을 문자. 기본값은 공백.

   ```python
   original_str = "Hello"
   padded_str = original_str.rjust(10)
   # 출력: '     Hello'
   ```

2. **`zfill(width)`**:
   - 문자열의 왼쪽에 '0'을 추가하여 문자열의 폭(길이)을 맞춥니다.
   - `width`: 최종 문자열의 폭(길이)을 나타내는 정수값.

   ```python
   number = 42
   binary_string = bin(number)[2:].zfill(8)
   # 출력: '00101010'
   ```

두 메서드 모두 문자열의 길이를 지정된 값으로 맞춰주는 역할을 하며, 사용하는 상황에 따라 적절한 메서드를 선택하여 활용할 수 있습니다.
