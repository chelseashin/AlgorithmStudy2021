# 핵심
괄호 안에 0 쌍, 괄호 밖에 3 쌍을 놓는 경우 - memo[0] * memo[3]
괄호 안에 1 쌍, 괄호 밖에 2 쌍을 놓는 경우 - memo[1] * memo[2]
괄호 안에 2 쌍, 괄호 밖에 1 쌍을 놓는 경우 - memo[2] * memo[1]
괄호 안에 3 쌍, 괄호 밖에 0 쌍을 놓는 경우 - memo[3] * memo[0]
출처: https://velog.io/@tmdgh0221/%EB%B0%B1%EC%A4%80-10422%EB%B2%88-%EA%B4%84%ED%98%B8