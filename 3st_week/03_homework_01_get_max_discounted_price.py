# Q. 쓱 최대로 할인 적용하기
# 다음과 같이 숫자로 이루어진 배열이 두 개가 있다.
# 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다.
# 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다.
# 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다

# 문제 분석
# 1. 숫자 배열이 두 개가 주어진다
# 2. 하나는 상품의 가격, 하나는 쿠폰을 담은 배열
# 3. 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다
# 4. 최대한 할인을 많이 받는 케이스라면 얼마를 내야 하는가?
# 5. *단 할인 쿠폰은 한 제품에 한 번만 적용할 수 있다

# 아이디어
# 상품의 가격이 주어지고 할인율이 주어졌다. 그리고 할인 쿠폰은 한 제품에 한 번만 적용 가능하다
# 당연히 상품의 가격이 크면 할인율이 큰 쿠폰을 사용하면 이득이다
# 주의점은 상품이 몇 개인지 할인 쿠폰이 몇 개인지 랜덤이라는 점이다 뭐가 먼저 끝날지 모른다
# -> 상품이 기준이 돼야한다

# 풀이방법
# 상품을 내림차순으로 정렬한다, 할인율도 같은 방식으로 정렬한다 큰 값에 큰 할인율을 적용할 수 있게 한다
# 상품 배열의 길이만큼 돌린다
# 원래 가격 - (원래 가격 * 할인율/ 100) 을 sum이란 값에 저장한다
# 쿠폰의 길이보다 인덱스가 커지면 종료한다
# 쿠폰이 없는 경우도 생각해야 한다

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 내 풀이
def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    coupons_last_index = len(coupons) - 1

    sum = 0

    for i in range(len(prices)):
        if coupons_last_index < i:
            for j in range(i, len(prices)): # 이중 for 문 아님!
                sum += prices[j]
            return sum
        # print("price : ", prices[i], "coupon : ", coupons[i])
        sum += (prices[i] - (prices[i] * coupons[i]//100))

    return sum


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))