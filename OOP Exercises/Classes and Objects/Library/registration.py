from project.user import User
from project.library import Library


class Registration:
    def add_user(self, user: User, library: Library) -> None or str:
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library) -> None or str:
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:
        for person in library.user_records:
            if person.user_id == user_id:
                if person.username == new_username:
                    return "Please check again the provided username" \
                           " - it should be different than the username used so far!"

                current_idx = library.user_records.index(person)
                current_name = person.username
                person.username = new_username
                library.user_records[current_idx] = person

                for renter in library.rented_books:
                    if renter == current_name:
                        current_rented = library.rented_books[renter]
                        del library.rented_books[renter]
                        renter = new_username
                        library.rented_books[renter] = current_rented
                return f"Username successfully changed to: {new_username} for user id: {user_id}"

            return f"There is no user with id = {user_id}!"
