DROP TABLE RoleProfil;
DROP TABLE RoleGroup;
DROP TABLE Account;
DROP TABLE Person;
DROP TABLE Profil;

CREATE TABLE RoleProfil
(
  roleprofil_id INT NOT NULL,
  roleprofil_label VARCHAR(50) NOT NULL,
  CONSTRAINT PK_roleprofil_id PRIMARY KEY (roleprofil_id)
);

CREATE TABLE RoleGroup
(
  rolegroup_id INT NOT NULL,
  rolegroup_label VARCHAR(50) NOT NULL,
  CONSTRAINT PK_rolegroup_id PRIMARY KEY (rolegroup_id)
);

CREATE TABLE Nationality
(
  nationality_id INT NOT NULL,
  nationality_label VARCHAR(100) NOT NULL,
  CONSTRAINT PK_nationality_id PRIMARY KEY (nationality_id)
);

CREATE TABLE Genre
(
  genre_id INT NOT NULL,
  genre_label VARCHAR(50) NOT NULL,
  CONSTRAINT PK_genre_id PRIMARY KEY (genre_id)
);

CREATE TABLE Account
(
  account_id INT NOT NULL,
  account_email VARCHAR(100) NOT NULL,
  account_login VARCHAR(100) NOT NULL,
  account_password VARCHAR(255) NOT NULL,
  account_date_create DATETIME NOT NULL,
  account_last_connexion DATETIME NOT NULL,
  CONSTRAINT PK_account_id PRIMARY KEY (account_id)
);

CREATE TABLE Person
(
  person_id INT NOT NULL,
  person_firstname VARCHAR(100) NOT NULL,
  person_lastname VARCHAR(100) NOT NULL,
  person_image VARCHAR(255) NULL,
  person_birth_date DATE NULL,
  person_nationality INT NULL,
  CONSTRAINT PK_person_id PRIMARY KEY (person_id),
  CONSTRAINT FK_person_nationality FOREIGN KEY (person_nationality) REFERENCES Nationality(nationality_id)
);

CREATE TABLE Celebrity
(
  celebrity_id INT NOT NULL,
  celebrity_bio TEXT NULL,
  celebrity_person NOT NULL,
  CONSTRAINT PK_celebrity_id PRIMARY KEY (celebrity_id),
  CONSTRAINT FK_celebrity_person FOREIGN KEY (celebrity_person) REFERENCES Person(person_id)
);

CREATE TABLE Profil
(
  profil_id INT NOT NULL,
  profil_role INT NOT NULL,
  profil_account INT NOT NULL,
  profil_mediatek INT NOT NULL,
  CONSTRAINT PK_profil_id PRIMARY KEY (profil_id),
  CONSTRAINT FK_profil_role FOREIGN KEY (profil_role) REFERENCES RoleProfil(roleprofil_id),
  CONSTRAINT FK_profil_account FOREIGN KEY (profil_account) REFERENCES Account(account_id)
);

CREATE TABLE TypeMedia
(
  typemedia_id INT NOT NULL,
  typemedia_label VARCHAR(100) NOT NULL,
  CONSTRAINT PK_typemedia_id PRIMARY KEY (typemedia_id)
);

CREATE TABLE Media
(
  media_id INT NOT NULL,
  media_type INT NOT NULL,
  media_title VARCHAR(100) NOT NULL,
  media_synopsis TEXT NULL,
  media_image VARCHAR(255) NULL,
  media_nationality INT NULL,
  media_original_title VARCHAR(100) NULL,
  media_release_date DATE NULL,
  media_certification INT NULL,
  CONSTRAINT PK_media_id PRIMARY KEY (media_id),
  CONSTRAINT FK_media_type FOREIGN KEY (media_type) REFERENCES TypeMedia(typemedia_id),
  CONSTRAINT FK_media_nationality FOREIGN KEY (media_nationality) REFERENCES Nationality(nationality_id)
);

CREATE TABLE Episode
(
  episode_id INT NOT NULL,
  episode_media INT NOT NULL,
  episode_number INT NOT NULL,
  episode_season INT NOT NULL,
  episode_parent INT NOT NULL,
  CONSTRAINT PK_episode_id PRIMARY KEY (episode_id),
  CONSTRAINT FK_episode_media FOREIGN KEY (episode_media) REFERENCES Media(media_id)
  CONSTRAINT FK_episode_parent FOREIGN KEY (episode_parent) REFERENCES Media(media_id)
);

CREATE TABLE MediaGenre
(
  mediagenre_id INT NOT NULL,
  mediagenre_media INT NOT NULL,
  mediagenre_genre INT NOT NULL,
  CONSTRAINT PK_mediagenre_id PRIMARY KEY (mediagenre_id),
  CONSTRAINT FK_mediagenre_media FOREIGN KEY (mediagenre_media) REFERENCES Media(media_id),
  CONSTRAINT FK_mediagenre_genre FOREIGN KEY (mediagenre_genre) REFERENCES Genre(genre_id)
);

CREATE TABLE Score
(
  score_id INT NOT NULL,
  score_media INT NOT NULL,
  score_profil INT NOT NULL,
  score_comment TEXT NULL,
  CONSTRAINT PK_score_id PRIMARY KEY (score_id),
  CONSTRAINT FK_score_media FOREIGN KEY (score_media) REFERENCES Media(media_id),
  CONSTRAINT FK_score_profil FOREIGN KEY (score_profil) REFERENCES Profil(profil_id)
);
