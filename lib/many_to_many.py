class Author:
    all = []
    
    
    
    def __init__(self, name,):
        self.name = name
        
        self.book_list= []
        self.contract_list = []

    

    def contracts(self):

        return self.contract_list
        
        
    
    def books(self):
        return self.book_list
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        result = 0
        for contract in self.contract_list:
            if contract.author is self:
                result += contract.royalties
        return result
        

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        self.contract_list = []
        self.author_list = []

    def contracts(self):
        return self.contract_list
    
    def authors(self):
        return self.author_list
    




class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("failed")
        if not isinstance(book, Book):
            raise Exception("failed")
        if not isinstance(date, str):
            raise Exception("failed")
        if not isinstance(royalties, int):
            raise Exception('failed')

    

        self.author = author
        self.book = book
        self.date = date
        self.royalties= royalties
        Contract.all.append(self)
        author.contract_list.append(self)
        book.contract_list.append(self)
        author.book_list.append(book)
        book.author_list.append(author)

    @classmethod 
    def contracts_by_date(cls, date):
        date_list= []
        for contract in cls.all:
            if contract.date == date:
                date_list.append(contract)
        return date_list

