# Snippets

## Index
- Change pnd icon color from drawable resources or runtime [link](#Change-pnd-icon-color-from-drawable-resources-or-runtime)
- Remove notification bar and make app full screen[link]()


#### Change pnd icon color from drawable resources or runtime
```
 Drawable mIcon= ContextCompat.getDrawable(getActivity(), R.drawable.your_icon);
    mIcon.setColorFilter(ContextCompat.getColor(getActivity(), R.color.new_color), PorterDuff.Mode.MULTIPLY);
    mImageView.setImageDrawable(mIcon);
```
```
drawable = DrawableCompat.wrap(drawable);
DrawableCompat.setTint(drawable, color);
```

#### Remove notification bar and make app full screen
```
WindowManager.LayoutParams attrs = this.getWindow().getAttributes();
        attrs.flags |= WindowManager.LayoutParams.FLAG_FULLSCREEN;
        this.getWindow().setAttributes(attrs);
```
Place this code in MainActivity OnCreate()