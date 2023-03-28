from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO menu_treemenucategory (id, name, verbose_name) 
                VALUES (1, 'main_menu', 'Main menu');

            INSERT INTO menu_treemenu (id, name, path, category_id, parent_id) 
                VALUES (1, 'Home', 'home', 1, null);
            INSERT INTO menu_treemenu (id, name, path, category_id, parent_id) 
                VALUES (2, 'News', 'news', 1, null);
            INSERT INTO menu_treemenu (id, name, path, category_id, parent_id) 
                VALUES (3, 'About', 'about', 1, null);
            INSERT INTO menu_treemenu (id, name, path, category_id, parent_id) 
                VALUES (4, 'Contacts', 'contacts', 1, 3);
            INSERT INTO menu_treemenu (id, name, path, category_id, parent_id) 
                VALUES (5, 'Careers', 'careers', 1, 4);
            INSERT INTO menu_treemenu (id, name, path, category_id, parent_id) 
                VALUES (6, 'Media', 'media', 1, 4);
            INSERT INTO menu_treemenu (id, name, path, category_id, parent_id) 
                VALUES (7, 'Events', 'events', 1, null);
            INSERT INTO menu_treemenu (id, name, path, category_id, parent_id) 
                VALUES (8, 'Webinars', 'webinars', 1, 7);
            INSERT INTO menu_treemenu (id, name, path, category_id, parent_id) 
                VALUES (9, 'Foreign source - Github', 'https://github.com/Defa-TReS2b', 1, 7);
            INSERT INTO menu_treemenu (id, name, path, category_id, parent_id) 
                VALUES (10, 'Foreign source - YouTube', 'https://www.youtube.com/', 1, 7);
        """)
    ]
