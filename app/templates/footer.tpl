{% extends 'base.tpl' %}
{% block footer %}
    <script
        src="{{ url_for('static', filename='assets/js/lib/jquery-2.1.3.min.js')}}
    ></script>
    <script
        src="{{ url_for('static', filename='assets/js/jquery.mousewheel.min.js')}}
    ></script>
    <script
        src="{{ url_for('static', filename='assets/js/jquery.cookie.min.js')}}
    ></script>
    <script
        src="{{ url_for('static', filename='assets/js/fastclick.min.js')}}
    ></script>
    <script
        src="{{ url_for('static', filename='assets/js/bootstrap.min.js')}}
    ></script>
    <script
        src="{{ url_for('static', filename='assets/js/clearmin.min.js')}}
    ></script>
{% endblock %}
