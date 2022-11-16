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

    # IMAGE
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
    def toContent(self):
        return self.__ns.model('BlogContent', {
            'time': fields.String('timestamp'),
            'version': fields.String('EDITORJS VERSION'),
            'blocks': fields.String('Array of Objects containing data to form HTML elements')
        })
    
    # BLOG
    def toCreateBlog(self):
        return self.__ns.model(
            'CreateBlog', {
                'title': fields.String('title'),
                'description': fields.String('description'),
                'image': fields.Nested(self.toBlogImage()),
                'author': fields.Nested(self.toAuthor()),
                'content': fields.Nested(self.toContent()),
                'created_at': fields.DateTime(),
                'updated_at': fields.DateTime(),
            }
        )