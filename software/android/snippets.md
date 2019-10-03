# Snippets

## Index

* [Change png icon color from drawable resources or runtime ](snippets.md#Change-png-icon-color-from-drawable-resources-or-runtime)
* [Remove notification bar and make app full screen](snippets.md#Remove-notification-bar-and-make-app-full-screen)
* [Add dialog box for alert](snippets.md#Add-dialog-box-for-alert)

### Change png icon color from drawable resources or runtime

```text
 Drawable mIcon= ContextCompat.getDrawable(getActivity(), R.drawable.your_icon);
    mIcon.setColorFilter(ContextCompat.getColor(getActivity(), R.color.new_color), PorterDuff.Mode.MULTIPLY);
    mImageView.setImageDrawable(mIcon);
```

```text
drawable = DrawableCompat.wrap(drawable);
DrawableCompat.setTint(drawable, color);
```

### Remove notification bar and make app full screen

```text
WindowManager.LayoutParams attrs = this.getWindow().getAttributes();
        attrs.flags |= WindowManager.LayoutParams.FLAG_FULLSCREEN;
        this.getWindow().setAttributes(attrs);
```

Place this code in MainActivity OnCreate\(\)

### Add dialog box for alert

```text
AlertDialog.Builder builder1 = new AlertDialog.Builder(context);
builder1.setMessage("Write your message here.");
builder1.setCancelable(true);

builder1.setPositiveButton(
    "Yes",
    new DialogInterface.OnClickListener() {
        public void onClick(DialogInterface dialog, int id) {
            dialog.cancel();
            /* DoSomethingWhenUserSaysYes() */
        }
    });

builder1.setNegativeButton(
    "No",
    new DialogInterface.OnClickListener() {
        public void onClick(DialogInterface dialog, int id) {
            dialog.cancel();
            /* DoSomethingWhenUserSaysNo() */
        }
    });

AlertDialog alert11 = builder1.create();
alert11.show();
```

