from django.contrib.auth import get_user_model


User = get_user_model()


class UserBackend(object):
    def authenticate(self, request, email=None):
        print("검증")
        print(email)

        if email:  # 클라이언트에서 카카오로그인 성공시
            try:  # 유저가 있는 경우
                user = User.objects.get(username=email)
                print("유저확인")
            except User.DoesNotExist:  # 유저 정보가 없지만 인증 통과시 user 생성
                print("회원생성")
                phone = request.data.get("phone")
                email = request.data.get("email")
                firstName = request.data.get("firstName")
                policy = request.data.get("policy")
                servicepolicy = request.data.get("servicepolicy")
                user = User.objects.create(
                    username=email,
                    email=email,
                    first_name=firstName,
                    phone=phone,
                    policy=policy,
                    servicepolicy=servicepolicy,
                )
                user.is_staff = False
                user.is_superuser = False
                user.save()
                # 여기서는 user.password를 저장하는 의미가 없음.(장고가 관리 못함)
            return user

        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)  # 유저를 pk로 가져온다
        except User.DoesNotExist:
            return None
