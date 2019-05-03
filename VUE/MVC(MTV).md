# MVC(MTV)

M - Model(models.py)

V - View(Template.html)

C - Controller(views.py)

# MVVM

M - Model

V - View(HTML)

VM - View-Model(Vue)



```html
# 조건
{% if post.is_public %}
	{{ post }}
{% endif %}

# 반복
{% for post in posts %}
	{{ post }}
{% endfor %}
```



# Vue Directive

```html
<!-- 조건 -->
<p v-if='posts.isPublic'>
   	{{ post }}
</p>

<!-- 반복 -->
<ul>
    <li v-for='post in posts'>
    	{{ post }}
    </li>
</ul>
```

