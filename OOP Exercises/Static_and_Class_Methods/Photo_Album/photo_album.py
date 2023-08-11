from typing import List


class PhotoAlbum:

    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: List[List[str]] = self.__initialize_photos()

    def __initialize_photos(self) -> List[List[str]]:
        photos = [[] for _ in range(0, self.pages)]
        return photos

    @classmethod
    def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
        if photos_count <= 4:
            pages = 1
        else:
            pages = photos_count // 4 if photos_count % 4 == 0 else photos_count // 4 + 1

        return cls(pages)

    def add_photo(self, label: str) -> str:
        for page_no in range(self.pages):
            if len(self.photos[page_no]) < 4:
                self.photos[page_no].append(label)
                return f"{label} photo added successfully on page {page_no + 1} slot {len(self.photos[page_no])}"

        return "No more free slots"

    def display(self) -> str:

        if self.pages > 0:
            result = f"-----------"
            for page in self.photos:
                result += f"\n{' '.join(['[]' for _ in page])}" + f"\n-----------"

            return result

# class PhotoAlbum:

#     def __init__(self, pages: int) -> None:
#         self.pages = pages
#         self.photos = [[] for _ in range(0, self.pages)]

#     @classmethod
#     def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
#         if photos_count <= 4:
#             pages = 1
#         else:
#             pages = photos_count // 4 if photos_count % 4 == 0 else photos_count // 4 + 1

#         return cls(pages)

#     def add_photo(self, label: str) -> str:
#         for page_no in range(self.pages):
#             if len(self.photos[page_no]) < 4:
#                 self.photos[page_no].append(label)
#                 return f"{label} photo added successfully on page {page_no + 1} slot {len(self.photos[page_no])}"

#         return "No more free slots"

#     def display(self) -> str:

#         if self.pages > 0:
#             result = f"-----------"
#             for page in self.photos:
#                 result += f"\n{' '.join(['[]' for _ in page])}" + f"\n-----------"

#             return result
