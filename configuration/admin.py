from django.contrib import admin
from django.utils.html import mark_safe


from .models import Configuration



# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    """Base class to be inherited to if image fields need to be shown as images."""

    # image_fields is a list or tuple of all fields whose images need
    # to be displayed
    # Child classes need to override this
    image_fields = []

    def get_image(self, field):
        """Get valid html for the image"""
        # field must be an instance of models.ImageField or at least a model.FileField
        if field:
            return mark_safe(
                f'<img style="object-fit:cover; object-position: center;" width="200px" height="200px" src="{field.url}">'
            )
        return ""

    def get_form(self, request, obj, *args, **kwargs):
        # We call the overriden get_form method so it generates the required
        # form data for us and override only those we need to.
        form = super().get_form(request, obj, *args, **kwargs)
        # Ensure that there is already an object
        # before trying to show the image.
        if not obj:
            return form

        # Display the image at the bottom of the help_text
        # if the object is in the database
        for field in self.image_fields:
            # for a nice display, I chose to override the help text instead.
            # it makes the image show right beneath the the input tags. It's lovely
            try:
                form.base_fields[field].help_text = mark_safe(
                    "".join(
                        [
                            "<div>",
                            form.base_fields[field].help_text,
                            f"</div><div style='padding: 10px 0;'>{self.get_image(getattr(obj, field))}</div>",
                        ]
                    )
                )
            except:
                pass
            
        return form

# Register your models here.
@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    pass