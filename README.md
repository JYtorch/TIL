# TIL

> Today I learned



user@DESKTOP-F4VHJPH MINGW64 ~
$ mkdir TIL

user@DESKTOP-F4VHJPH MINGW64 ~
$ cd TIL

user@DESKTOP-F4VHJPH MINGW64 ~/TIL
$ ls

user@DESKTOP-F4VHJPH MINGW64 ~/TIL
$ touch test.md

user@DESKTOP-F4VHJPH MINGW64 ~/TIL
$ rm test.md

user@DESKTOP-F4VHJPH MINGW64 ~/TIL
$ touch README.md

user@DESKTOP-F4VHJPH MINGW64 ~/TIL
$

user@DESKTOP-F4VHJPH MINGW64 ~/TIL
$ git init
Initialized empty Git repository in C:/Users/user/TIL/.git/

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ ls
README.md

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ ls -a
./  ../  .git/  README.md

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ cd ..

user@DESKTOP-F4VHJPH MINGW64 ~
$ cd TIL

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git add README.md

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git commit -m "add README.md"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'user@DESKTOP-F4VHJPH.(none)')

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git config --global user.name JYA

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git config --global user.name
JYA

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git config --global user.email abogado2113@gmail.com

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git config --global user.email
abogado2113@gmail.com

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git commit -m "add README.md"
[master (root-commit) e8e4a5b] add README.md
 1 file changed, 6 insertions(+)
 create mode 100644 README.md

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git log
commit e8e4a5b09be5bb8e14b992f9646788aeab123f75 (HEAD -> master)
Author: JYA <abogado2113@gmail.com>
Date:   Thu Jul 15 11:08:22 2021 +0900

    add README.md

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git remote add origin https://github.com/JYtorch/TIL.git

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git push origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 242 bytes | 121.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/JYtorch/TIL.git
 * [new branch]      master -> master

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$





--------------------------------------------------

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ cd git/

user@DESKTOP-F4VHJPH MINGW64 ~/TIL/git (master)
$ cd ..

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git add .

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
        new file:   git/command.md
        modified:   linux/command.md


user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git commit -m "add git/command.md"
[master 72549c4] add git/command.md
 3 files changed, 220 insertions(+), 3 deletions(-)
 create mode 100644 git/command.md

user@DESKTOP-F4VHJPH MINGW64 ~/TIL (master)
$ git push origin master
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (7/7), 1.90 KiB | 486.00 KiB/s, done.
Total 7 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/JYtorch/TIL.git
   0122588..72549c4  master -> master

-----------

`request.get(url) `  크롬에서 url주소를 입력하는 것과 같은 효과

