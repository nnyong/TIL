const app = new Vue({
  el: "#app",
  data: {
    logo: 'MO<i class="fab fa-vuejs"></i>IE',
    isMain: true,
    genres: [],
    movies: [  // 현재 하드 타이핑 된 배열이지만, 실제로는 axios.get() 을 통해 API server 로 부터 받아옵니다.
      {
        "id": 1,
        "title": "자전차왕 엄복동",
        "audience": 168860,
        "poster_url": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1590/159070_P13_114738.jpg",
        "description": "일제강점기, 일본에서는 조선의 민족의식을 꺾고 그들의 지배력을 과시하기 위해 전조선자전차대회를 개최한다. 하지만 일본 최고의 선수들을 제치고 조선인 최초로 우승을 차지한 엄복동의 등장으로 일본의 계략은 실패로 돌아가고...",
        "genreId": 3,
      },
      {
        "id": 2,
        "title": "항거:유관순 이야기",
        "audience": 1041939,
        "poster_url": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1823/182360_P11_140223.jpg",
        "description": "1919년 3.1 만세운동 후 세평도 안 되는 서대문 감옥 8호실 속, 영혼만은 누구보다 자유로웠던 유관순과 8호실 여성들의 1년의 이야기.",
        "genreId": 3
      },
    ],
    search: '', // 검색 기능을 구현할 때, 사용자의 입력 값을 이곳에 쌍방향 바인딩 합니다.

    detailView: false, // 현재 방식의 목록/상세 화면 전환에 사용되는 flag 입니다.
    movieDetail: {},  // 상세 화면에서 출력할 때 사용할 영화 객체입니다.
  },
  methods: {
    toggleDetail: function(id=null) {  // 목록 <=> 상세 화면을 전환합니다. 인자로 id 가 들어올 경우, 상세화면을 표시합니다.
      if (id) {
        const movie = this.movies[0]  // 현재는 무조건 $data.movies 의 첫 번째 영화를 선택합니다. 실제로는 인자로 넘어온 id 를 통해 특정 영화를 찾습니다.

        // Better way..?
        this.movieDetail.title = movie.title
        this.movieDetail.audience= movie.audience
        this.movieDetail.poster_url= movie.poster_url
        this.movieDetail.description = movie.description

        this.movieDetail.scores = []  // 상세 페이지에서 표시할 모든 $data.scores 를 받아와야 합니다.
        this.movieDetail.genre = '' // 해당 movie 의 genreId 를 통해 genre.name 을 찾아서 저장합니다.
      }
      this.detailView = !this.detailView
    },
  },
  computed: {},

  watch: {},

  created: function () {  // Vue 인스턴스가 생성되는 시점에 실행되는 함수입니다. 현재는 Vue 인스턴스가 생성되면, API 서버에서 장르목록만 받아옵니다.
      axios.get(`${HOST}/genres`)  // 만약 API 서버를 사용하지 않거나 서버가 꺼져있다면 에러가 발생합니다.
        .then(res => this.genres = res.data)
  }
});
