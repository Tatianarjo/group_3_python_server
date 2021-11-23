CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

INSERT INTO `Users` VALUES (null, 'Peaches', 'Dasha', 'peaches@email.com', 'puppy', 'Peaches1', '1234', 'url', 2021-11-01, 1);
INSERT INTO `Users` VALUES (null, 'Tatiana', 'Johnson', 'tatiana@email.com', 'glitter', 'eyepissglitter', '123456', 'url', 2021-11-01, 1);
INSERT INTO `Users` VALUES (null, 'Emma', 'Vogelmeier', 'emma@email.com', 'I exist!', 'Emma123', '54321', 'url', 2021-11-01, 1);
INSERT INTO `Users` VALUES (null, 'Zach', 'Wiley', 'zach@email.com', 'I am here.', 'Zach345', '6789', 'url', 2021-11-01, 1);
INSERT INTO `Users` VALUES (null, 'Jackie', 'Gregory', 'jackie@email.com', 'This is my profile.', 'Jackie789', '7654', 2021-11-01, 1)


INSERT INTO `Posts` VALUES (null, 1, 1, 'My first post!', 2021-11-03, 'url', 'content', 1);
INSERT INTO `Posts` VALUES (null, 2, 3, 'Another post!', 2021-11-04, 'url', 'content', 1);
INSERT INTO `Posts` VALUES (null, 3, 5, 'And another post!', 2021-11-05, 'url', 'content', 1);
INSERT INTO `Posts` VALUES (null, 4, 6, 'Here is something else!', 2021-11-08, 'url', 'content', 1);
INSERT INTO `Posts` VALUES (null, 5, 7, 'More info!', 2021-11-09, 'url', 'content', 1);


INSERT INTO `Categories` VALUES (null, 'candles')
INSERT INTO `Categories` VALUES (null, 'flowers')
INSERT INTO `Categories` VALUES (null, 'puppies')
INSERT INTO `Categories` VALUES (null, 'hair')


INSERT INTO Users values(null, 'Peaches', 'Dasha', 'peaches@email.com', 'puppy', 'Peaches1', 1234, 'url', 2021-11-01, 1)

DELETE FROM Users
--remember to delete from users then register our users
SELECT * FROM Users

SELECT * FROM Categories

