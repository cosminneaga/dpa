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
            'git_hub': fields.String('github-profile-url'),
            'git_gists': fields.List(fields.Nested(self.toAuthor__authorLinksObject())),
            'others': fields.List(fields.Nested(self.toAuthor__authorLinksObject()))
        })


    def toAuthor__authorLinksObject(self):
        return self.__ns.model('authorLinksObject', {
            'text': fields.String('link-display-text'),
            'url': fields.String('link-url')
        })

    # CONTENT
    def toContent(self):
        return self.__ns.model('BlogContent', {
            'type': fields.String('text / image'),
            'style': fields.List(fields.Nested(self.toContent__contentStyle())),
            'content': fields.String('if "type" text use this to fill with text content'),
            'caption': fields.String('if "type" image use this to create image caption')
        })

    def toContent__contentStyle(self):
        return self.__ns.model('contentStyle', {
            'type': fields.String('text-align'),
            'action': fields.String('center')
        })
    
    # BLOG
    def toCreateBlog(self):
        return self.__ns.model(
            'CreateBlog', {
                'title': fields.String('title'),
                'description': fields.String('description'),
                'image': fields.Nested(self.toBlogImage()),
                'date': fields.DateTime(),
                'author': fields.Nested(self.toAuthor()),
                'content': fields.List(fields.Nested(self.toContent()))
            }
        )