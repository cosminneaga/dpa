export interface BlogMeta {
    title: string;
    description: string;
    image: {
        src: string;
        alt: string;
        title: string;
    };
    author: {
        name: string;
        links: [
            {
                text: string;
                url: string;
                image: string;
            }
        ];
    };
    category: string;
    tags: string[];
    content: object[];
}

export interface AuthorLink {
    text: string;
    url: string;
    image: string;
}

export interface ComponentData {
    meta: BlogMeta;
}
