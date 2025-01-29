# // inputan user

user_input = {
    "tema": "{inputan_user}",
    "subtema": {
      {inputan_user}
    },
    "muatan_terpadu": "{inputan_user}",
    "pembelajaran_ke": {
        {inputan_user}
    },
    
}


user_input = {
    "tema": "Pecahan",
    "subtema": {
        "subtema1": "Pengenalan Pecahan",
        "subtema2": "Operasi Pecahan",
        "subtema3": "Perbandingan Pecahan Sederhana dan Penyerdehanaan Pecahan"
    },
    "muatan_terpadu": "Matematika",
    "pembelajaran_ke": {
        "pembelajaran1": 1,
        "pembelajaran2": 2,
        "pembelajaran3": 3
    },
    
}

# // template prompt / optimalisasi
optimalisasi = {

}

# // response renerative AI
response = {
    "tujuan_pembelajaran": "{response_ai}",
   "data": {
     "pendahuluan": {
    "kegiatan": [
    {
        "deskripsi": "{response_ai}",
        "alokasi_waktu": "{response_ai}"
    },
    ],
    "total_alokasi_waktu": "{response_ai}"
    },
    "kegiatan_inti": {
      "model": "{response_ai}",
      "sub_kegiatan": [
        {
          "judul": "{response_ai}",
          "kegiatan": [
            {
              "deskripsi": "{response_ai}",
              "alokasi_waktu": "{response_ai}",
              "kategori": "{response_ai}"
            },
          ]
        },
      ],
      "total_alokasi_waktu": "{response_ai}"
    },
    "penutup": {
      "kegiatan": [
        {
          "deskripsi": "{response_ai}",
          "alokasi_waktu": "{response_ai}"
        },
        {
          "deskripsi": "{response_ai}",
          "alokasi_waktu": "{response_ai}"
        },
      ],
      "total_alokasi_waktu": "{response_ai}"
   }
    }
}