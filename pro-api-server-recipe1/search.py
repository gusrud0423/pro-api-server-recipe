#  인증 토큰 이용해서 로그인 하기

# 포스트맨에서는  회원가입하는 api >>  로그인 api 에서  회원 가입한 이메일과 패스워드를 치고  샌드 하면
# 토큰이 생기고  이 토큰 복사해서 
# 레시피 생성하는 api 가서  헤더 열고 맨 밑에  Authorization      Bearer 토큰복붙 하고 컨트롤 s 로 저장후 샌드 
# 누르면 err_code : 0 뜬다 에러 0은 새로운 레시피 추가하는 api 에서 인증토큰이 오류난것 ??


# 로그아웃시에는 다시 위에 토큰 가지고 헤더에 추가후 샌드 누르면 정상이면  로그아웃 되었다고 뜨고 만약 이상하면 로그인 다시 하고 해야함 
# 레시피 생성하는 api 가서 다시 그 토큰으로 샌드 누르면 "msg": "Token has been revoked"  이렇게 뜬다  이게 정상


#  "msg": "Token has expired" 이건 토큰이 만료 된것이니 다시 로그인 하여 토큰을 새로 받아야 한다 


# 로그인한게 user 테이블에서 id 가 10번 이면 생성된 토큰을 내정보가져오는 API 에 넣고  localhost:5003/users/10/my  이렇게 넣으면 실행이 맞게 되야하고 
                    # 만약 localhost:5003/users/11/my 이렇게 넣었을 때는  err_code : 1 이 나와야 한다 왜냐면 둘이 다른 아이디니까 

# 배포하는 것
#
                                                                # 이렇게 가지고올때 이걸 해주는 서비스가 있다 =서버리스 프레임워크 
# 플라스크로 앱 만든 모든 소스파일들 을 깃허브에 다 올려 그러면 그럴때 자동으로 aws에 클라우드가  소스파일들을 가지고 와 배포한다 (api gate way에 우리가 만든 경로들을 쓰고 파이썬 코드들을 람다에 넣는다 자동으로)
 # 이렇게 만들어 놓으면 몇만명이든 들어오면 AWS에서 알아서 스케일 아웃해서 서버를 여러개 만들고 스케일 업해서 람다를 업그레이드 하고 한다

 # 이렇게 우리가 쓰는 서비스는 깃허브 서비스, 서버리스 프레임워크 서비스, AWS 서비스 이다 

 # 이제 다 개발 했으니 1. 먼저 AWS 이용을 위한 , credentials 만들기
 # 그럴려면 aws에서 iam 써서 사용자 메뉴 들어가서 사용자 추가 
 # api_server 이름적는다 근데 이사용자는 무슨사용자 ? >> 소스파일들을 aws에 가지고 올때 이 접속시 관리하는 유저가 api_server 이다 
 # 프로그래밍 방식 액세스 , 콘솔 액세스 체크

# 피피티 데로 다하고 나면 서버리스 프레임워크 설치 >>다 넥스트 하고 인스톨~~``dd