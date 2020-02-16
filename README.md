# couplechat DB設計
## Users テーブル
|Column|Type|Options|
|------|----|-------|
|nickname|CharField|null: false|
|name|CharField|null: false|
|email|CharField||null: false|
|password|CharField|null: false|
|profile|RichTextUploadingField|null: true|
|image|ImageField|null: true|
|birthday|DateField|null: true|
|couple_id|ForeignKey|null: false, ForeignKey: false|

### Asociation
- has_many :messages
- has_many :channels
- belongs_to :couples

## Channels テーブル
|Column|Type|Options|
|------|----|-------|
|user_id|ForeignKe|null: false, ForeignKey: false|to=Users, on_delete=models.channels|
|couple_id|ForeignKe|null: false, ForeignKey: false|to=couple_user, on_delete=models.cannels|
|channel_name|CharField||null: false|
|created_at|DateField|

### Asociation
- belongs_to: user 
- belongs_to :couple
- has_many: messages
- has_many: categories

## Couples テーブル
|Column|Type|Options|
|------|----|-------|
|user_id|ForeignKe|null: false, foregin_key :true|
|channel_id|ForeignKe|null: false, foregin_key :true|
### Asociation
- has_many :channels
- has_many :users
- has_many :messages

## Messages テーブル
|Column|Type|Options|
|------|----|-------|
|talk|TextField|
|image|CharField|
|read|CharField|
|created_at|DateField|null: true|
|user_id|ForeignKe|null: false, foregin_key :true|
|channels_id|ForeignKe|null: false, ForeignKey: false|to=channels, on_delete=models.message|
### Asociation
- belongs_to :channel
- belongs_to :user
- belongs_to :category
- belongs_to :couple

## Message_saves テーブル
|Column|Type|Options|
|------|----|-------|
|message_id|ForeignKe|null: false, ForeignKey: false|to=message_saves, on_delete=models.message|
|user_id|ForeignKe|null: false, ForeignKey: false|to=,message_saves, on_delete=models.user|
### Asociation
- has_many :messages
- belongs_to :user

## Alubams
|Column|Type|Options|
|------|----|-------|
|image_id|ForeignKe|null: false, ForeignKey: false|to=message_saves, on_delete=models.message|
### Asociation
- has_many :messages
- has_many :images
- belongs_to :user

## Images
|Column|Type|Options|
|------|----|-------|
|image|ImageField|null: false, ForeignKey: false|to=message_saves, on_delete=models.message|
|user_id|ForeignKe|null: false, ForeignKey: false|to=message_saves, on_delete=models.message|
### Asociation
- belongs_to :user
- belongs_to :alubam

## Category テーブル
|Column|Type|Options|
|------|----|-------|
|name|CharField|null: false|
### Asociation
- has_many :messages
- has_many :channels



