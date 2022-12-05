from flask_restx import fields


class BlogModel:

    def __init__(self, ns):
        self.__ns = ns

    # IMAGE
    def toBlogImage(self):
        return self.__ns.model('BlogImage', {
                'src': fields.String('image-src'),
                'alt': fields.String('image-alt-attribute'),
                'title': fields.String('image-title-attribute')
            }
        )

    # AUTHOR
    def toAuthor(self):
        return self.__ns.model('BlogAuthor', {
            'name': fields.String('author-name'),
            'links': fields.List(fields.Nested(self.toAuthor__authorLinks()))
        })

    def toAuthor__authorLinks(self):
        return self.__ns.model('authorLinks', {
            'text': fields.String('link display text'),
            'url': fields.String('link url'),
            'logo': fields.String('link logo'),
            'image': fields.String('link image')
        })

    # CONTENT
    # def toContent(self):
    #     return self.__ns.model('BlogContent', {
    #         # 'time': fields.String('timestamp'),
    #         # 'version': fields.String('EDITORJS VERSION'),
    #         # 'blocks': fields.String('Array of Objects containing data to form HTML elements')
    #         "insert": fields.String('sample insert text'),
    #         "attributes": fields.Nested(fields.String('sample'))
    #     })
    
    # MODEL
    def toCreateBlog(self):
        return self.__ns.model(
            'CreateBlog', {
                'title': fields.String('title'),
                'description': fields.String('description'),
                'image': fields.Nested(self.toBlogImage()),
                'author': fields.Nested(self.toAuthor()),
                'category': fields.String('category'),
                'tags': fields.List(fields.String('tags')),
                # 'content': [],
                'created_at': fields.DateTime(),
                'updated_at': fields.DateTime(),
            }
        )