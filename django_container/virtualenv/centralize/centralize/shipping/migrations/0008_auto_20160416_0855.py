# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-16 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0007_auto_20160416_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Any country'), ('UG', 'Uganda'), ('RW', 'Rwanda'), ('BY', 'Belarus'), ('MG', 'Madagascar'), ('NA', 'Namibia'), ('FO', 'Faroe Islands'), ('CL', 'Chile'), ('HM', 'Heard Island and McDonald Islands'), ('AQ', 'Antarctica'), ('AF', 'Afghanistan'), ('AL', 'Albania'), ('YT', 'Mayotte'), ('RE', 'Réunion'), ('BJ', 'Benin'), ('PH', 'Philippines'), ('ID', 'Indonesia'), ('TD', 'Chad'), ('SI', 'Slovenia'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('IE', 'Ireland'), ('AU', 'Australia'), ('MZ', 'Mozambique'), ('KN', 'Saint Kitts and Nevis'), ('US', 'United States of America'), ('MV', 'Maldives'), ('GW', 'Guinea-Bissau'), ('FR', 'France'), ('PW', 'Palau'), ('TG', 'Togo'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BG', 'Bulgaria'), ('BE', 'Belgium'), ('UM', 'United States Minor Outlying Islands'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('NF', 'Norfolk Island'), ('MW', 'Malawi'), ('CM', 'Cameroon'), ('KH', 'Cambodia'), ('NE', 'Niger'), ('CD', 'Congo (the Democratic Republic of the)'), ('GY', 'Guyana'), ('TJ', 'Tajikistan'), ('PK', 'Pakistan'), ('SO', 'Somalia'), ('DM', 'Dominica'), ('SC', 'Seychelles'), ('MC', 'Monaco'), ('MX', 'Mexico'), ('CW', 'Curaçao'), ('MR', 'Mauritania'), ('CR', 'Costa Rica'), ('GG', 'Guernsey'), ('MY', 'Malaysia'), ('TN', 'Tunisia'), ('MQ', 'Martinique'), ('IQ', 'Iraq'), ('GM', 'Gambia'), ('ML', 'Mali'), ('TC', 'Turks and Caicos Islands'), ('EE', 'Estonia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('TL', 'Timor-Leste'), ('ME', 'Montenegro'), ('BN', 'Brunei Darussalam'), ('HN', 'Honduras'), ('PE', 'Peru'), ('CO', 'Colombia'), ('GA', 'Gabon'), ('PN', 'Pitcairn'), ('CC', 'Cocos (Keeling) Islands'), ('NZ', 'New Zealand'), ('MU', 'Mauritius'), ('SL', 'Sierra Leone'), ('SN', 'Senegal'), ('BF', 'Burkina Faso'), ('PF', 'French Polynesia'), ('KP', "Korea (the Democratic People's Republic of)"), ('PY', 'Paraguay'), ('SZ', 'Swaziland'), ('GH', 'Ghana'), ('AD', 'Andorra'), ('GP', 'Guadeloupe'), ('VN', 'Viet Nam'), ('WS', 'Samoa'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('SS', 'South Sudan'), ('PS', 'Palestine, State of'), ('NI', 'Nicaragua'), ('IR', 'Iran (Islamic Republic of)'), ('LB', 'Lebanon'), ('GN', 'Guinea'), ('KM', 'Comoros'), ('AM', 'Armenia'), ('SB', 'Solomon Islands'), ('MH', 'Marshall Islands'), ('CF', 'Central African Republic'), ('TM', 'Turkmenistan'), ('CI', "Côte d'Ivoire"), ('FK', 'Falkland Islands  [Malvinas]'), ('RU', 'Russian Federation'), ('LY', 'Libya'), ('LA', "Lao People's Democratic Republic"), ('MN', 'Mongolia'), ('NC', 'New Caledonia'), ('JO', 'Jordan'), ('GL', 'Greenland'), ('KR', 'Korea (the Republic of)'), ('ER', 'Eritrea'), ('LR', 'Liberia'), ('GI', 'Gibraltar'), ('GS', 'South Georgia and the South Sandwich Islands'), ('SE', 'Sweden'), ('AR', 'Argentina'), ('EH', 'Western Sahara'), ('QA', 'Qatar'), ('TT', 'Trinidad and Tobago'), ('GU', 'Guam'), ('ST', 'Sao Tome and Principe'), ('MA', 'Morocco'), ('MO', 'Macao'), ('DO', 'Dominican Republic'), ('CV', 'Cabo Verde'), ('FJ', 'Fiji'), ('BB', 'Barbados'), ('MP', 'Northern Mariana Islands'), ('EG', 'Egypt'), ('BR', 'Brazil'), ('GF', 'French Guiana'), ('AX', 'Åland Islands'), ('CX', 'Christmas Island'), ('CH', 'Switzerland'), ('VC', 'Saint Vincent and the Grenadines'), ('SK', 'Slovakia'), ('AT', 'Austria'), ('PM', 'Saint Pierre and Miquelon'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('AE', 'United Arab Emirates'), ('RO', 'Romania'), ('LK', 'Sri Lanka'), ('ZW', 'Zimbabwe'), ('DJ', 'Djibouti'), ('MS', 'Montserrat'), ('MT', 'Malta'), ('TW', 'Taiwan (Province of China)'), ('GT', 'Guatemala'), ('GR', 'Greece'), ('AW', 'Aruba'), ('BO', 'Bolivia (Plurinational State of)'), ('TZ', 'Tanzania, United Republic of'), ('BS', 'Bahamas'), ('PA', 'Panama'), ('GE', 'Georgia'), ('VI', 'Virgin Islands (U.S.)'), ('EC', 'Ecuador'), ('DZ', 'Algeria'), ('DE', 'Germany'), ('HU', 'Hungary'), ('IO', 'British Indian Ocean Territory'), ('LC', 'Saint Lucia'), ('CY', 'Cyprus'), ('BD', 'Bangladesh'), ('PT', 'Portugal'), ('VA', 'Holy See'), ('TV', 'Tuvalu'), ('SX', 'Sint Maarten (Dutch part)'), ('FM', 'Micronesia (Federated States of)'), ('NU', 'Niue'), ('KE', 'Kenya'), ('KZ', 'Kazakhstan'), ('IT', 'Italy'), ('MF', 'Saint Martin (French part)'), ('LU', 'Luxembourg'), ('SD', 'Sudan'), ('HR', 'Croatia'), ('BI', 'Burundi'), ('CU', 'Cuba'), ('SJ', 'Svalbard and Jan Mayen'), ('CA', 'Canada'), ('CK', 'Cook Islands'), ('PR', 'Puerto Rico'), ('CN', 'China'), ('OM', 'Oman'), ('GD', 'Grenada'), ('UZ', 'Uzbekistan'), ('BL', 'Saint Barthélemy'), ('TK', 'Tokelau'), ('TF', 'French Southern Territories'), ('SG', 'Singapore'), ('JM', 'Jamaica'), ('NL', 'Netherlands'), ('PG', 'Papua New Guinea'), ('MM', 'Myanmar'), ('DK', 'Denmark'), ('YE', 'Yemen'), ('PL', 'Poland'), ('LT', 'Lithuania'), ('HK', 'Hong Kong'), ('TO', 'Tonga'), ('LS', 'Lesotho'), ('GQ', 'Equatorial Guinea'), ('RS', 'Serbia'), ('NG', 'Nigeria'), ('CG', 'Congo'), ('VG', 'Virgin Islands (British)'), ('SY', 'Syrian Arab Republic'), ('AS', 'American Samoa'), ('AZ', 'Azerbaijan'), ('JE', 'Jersey'), ('BV', 'Bouvet Island'), ('ES', 'Spain'), ('WF', 'Wallis and Futuna'), ('LI', 'Liechtenstein'), ('ZM', 'Zambia'), ('KI', 'Kiribati'), ('SM', 'San Marino'), ('KG', 'Kyrgyzstan'), ('IN', 'India'), ('ET', 'Ethiopia'), ('BZ', 'Belize'), ('BW', 'Botswana'), ('KY', 'Cayman Islands'), ('CZ', 'Czech Republic'), ('UA', 'Ukraine'), ('MD', 'Moldova (the Republic of)'), ('SR', 'Suriname'), ('JP', 'Japan'), ('SV', 'El Salvador'), ('TH', 'Thailand'), ('VU', 'Vanuatu'), ('NO', 'Norway'), ('TR', 'Turkey'), ('FI', 'Finland'), ('IS', 'Iceland'), ('BH', 'Bahrain'), ('AG', 'Antigua and Barbuda'), ('KW', 'Kuwait'), ('LV', 'Latvia'), ('AO', 'Angola'), ('ZA', 'South Africa'), ('HT', 'Haiti'), ('AI', 'Anguilla'), ('IM', 'Isle of Man'), ('BA', 'Bosnia and Herzegovina'), ('UY', 'Uruguay'), ('SA', 'Saudi Arabia'), ('IL', 'Israel')], default='', max_length=2),
        ),
    ]