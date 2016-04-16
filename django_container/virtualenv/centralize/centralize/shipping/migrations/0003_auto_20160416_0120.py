# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-16 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0002_auto_20160415_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethodcountry',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', 'Any country'), ('GD', 'Grenada'), ('BR', 'Brazil'), ('BY', 'Belarus'), ('AR', 'Argentina'), ('RO', 'Romania'), ('WF', 'Wallis and Futuna'), ('ST', 'Sao Tome and Principe'), ('CZ', 'Czech Republic'), ('SM', 'San Marino'), ('GU', 'Guam'), ('GG', 'Guernsey'), ('LV', 'Latvia'), ('TM', 'Turkmenistan'), ('LY', 'Libya'), ('ZA', 'South Africa'), ('SO', 'Somalia'), ('KN', 'Saint Kitts and Nevis'), ('EG', 'Egypt'), ('CN', 'China'), ('BI', 'Burundi'), ('AG', 'Antigua and Barbuda'), ('NZ', 'New Zealand'), ('NP', 'Nepal'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('YT', 'Mayotte'), ('RU', 'Russian Federation'), ('AT', 'Austria'), ('RW', 'Rwanda'), ('BF', 'Burkina Faso'), ('VU', 'Vanuatu'), ('MQ', 'Martinique'), ('GW', 'Guinea-Bissau'), ('FI', 'Finland'), ('FR', 'France'), ('GQ', 'Equatorial Guinea'), ('PM', 'Saint Pierre and Miquelon'), ('QA', 'Qatar'), ('SX', 'Sint Maarten (Dutch part)'), ('JO', 'Jordan'), ('LK', 'Sri Lanka'), ('CF', 'Central African Republic'), ('ES', 'Spain'), ('MW', 'Malawi'), ('GF', 'French Guiana'), ('BB', 'Barbados'), ('BJ', 'Benin'), ('VA', 'Holy See'), ('HT', 'Haiti'), ('MN', 'Mongolia'), ('MR', 'Mauritania'), ('NF', 'Norfolk Island'), ('TN', 'Tunisia'), ('AQ', 'Antarctica'), ('TL', 'Timor-Leste'), ('GR', 'Greece'), ('IL', 'Israel'), ('PR', 'Puerto Rico'), ('DZ', 'Algeria'), ('CG', 'Congo'), ('SR', 'Suriname'), ('ML', 'Mali'), ('NI', 'Nicaragua'), ('KP', "Korea (the Democratic People's Republic of)"), ('TR', 'Turkey'), ('PF', 'French Polynesia'), ('LB', 'Lebanon'), ('IN', 'India'), ('NO', 'Norway'), ('BA', 'Bosnia and Herzegovina'), ('ID', 'Indonesia'), ('AW', 'Aruba'), ('SI', 'Slovenia'), ('SV', 'El Salvador'), ('PK', 'Pakistan'), ('TF', 'French Southern Territories'), ('MS', 'Montserrat'), ('BD', 'Bangladesh'), ('SE', 'Sweden'), ('DO', 'Dominican Republic'), ('RE', 'Réunion'), ('MC', 'Monaco'), ('SS', 'South Sudan'), ('KI', 'Kiribati'), ('NU', 'Niue'), ('BG', 'Bulgaria'), ('FO', 'Faroe Islands'), ('NR', 'Nauru'), ('DM', 'Dominica'), ('TW', 'Taiwan (Province of China)'), ('DJ', 'Djibouti'), ('TC', 'Turks and Caicos Islands'), ('SK', 'Slovakia'), ('LS', 'Lesotho'), ('KH', 'Cambodia'), ('TJ', 'Tajikistan'), ('BN', 'Brunei Darussalam'), ('HU', 'Hungary'), ('GN', 'Guinea'), ('VN', 'Viet Nam'), ('GP', 'Guadeloupe'), ('TZ', 'Tanzania, United Republic of'), ('MF', 'Saint Martin (French part)'), ('PH', 'Philippines'), ('MU', 'Mauritius'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('ER', 'Eritrea'), ('AI', 'Anguilla'), ('CK', 'Cook Islands'), ('BO', 'Bolivia (Plurinational State of)'), ('SN', 'Senegal'), ('SG', 'Singapore'), ('TK', 'Tokelau'), ('MV', 'Maldives'), ('BZ', 'Belize'), ('GT', 'Guatemala'), ('CL', 'Chile'), ('LA', "Lao People's Democratic Republic"), ('EC', 'Ecuador'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('SZ', 'Swaziland'), ('GA', 'Gabon'), ('AZ', 'Azerbaijan'), ('CC', 'Cocos (Keeling) Islands'), ('EE', 'Estonia'), ('AX', 'Åland Islands'), ('CV', 'Cabo Verde'), ('BW', 'Botswana'), ('UG', 'Uganda'), ('TD', 'Chad'), ('NA', 'Namibia'), ('BL', 'Saint Barthélemy'), ('YE', 'Yemen'), ('AM', 'Armenia'), ('BH', 'Bahrain'), ('MA', 'Morocco'), ('AO', 'Angola'), ('PY', 'Paraguay'), ('PT', 'Portugal'), ('UM', 'United States Minor Outlying Islands'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('BT', 'Bhutan'), ('NG', 'Nigeria'), ('BM', 'Bermuda'), ('SB', 'Solomon Islands'), ('WS', 'Samoa'), ('GM', 'Gambia'), ('CD', 'Congo (the Democratic Republic of the)'), ('MH', 'Marshall Islands'), ('IR', 'Iran (Islamic Republic of)'), ('MT', 'Malta'), ('MZ', 'Mozambique'), ('HN', 'Honduras'), ('SA', 'Saudi Arabia'), ('VI', 'Virgin Islands (U.S.)'), ('FK', 'Falkland Islands  [Malvinas]'), ('LT', 'Lithuania'), ('PL', 'Poland'), ('IM', 'Isle of Man'), ('PE', 'Peru'), ('ZW', 'Zimbabwe'), ('VG', 'Virgin Islands (British)'), ('LC', 'Saint Lucia'), ('BE', 'Belgium'), ('GH', 'Ghana'), ('VC', 'Saint Vincent and the Grenadines'), ('HR', 'Croatia'), ('TT', 'Trinidad and Tobago'), ('FM', 'Micronesia (Federated States of)'), ('MY', 'Malaysia'), ('CU', 'Cuba'), ('NE', 'Niger'), ('SL', 'Sierra Leone'), ('LI', 'Liechtenstein'), ('LR', 'Liberia'), ('CI', "Côte d'Ivoire"), ('CX', 'Christmas Island'), ('GL', 'Greenland'), ('EH', 'Western Sahara'), ('PN', 'Pitcairn'), ('UY', 'Uruguay'), ('TH', 'Thailand'), ('GB', 'United Kingdom of Great Britain and Northern Ireland'), ('PA', 'Panama'), ('MX', 'Mexico'), ('GY', 'Guyana'), ('HK', 'Hong Kong'), ('SY', 'Syrian Arab Republic'), ('AL', 'Albania'), ('MD', 'Moldova (the Republic of)'), ('AU', 'Australia'), ('RS', 'Serbia'), ('SJ', 'Svalbard and Jan Mayen'), ('NC', 'New Caledonia'), ('IS', 'Iceland'), ('UZ', 'Uzbekistan'), ('KM', 'Comoros'), ('KR', 'Korea (the Republic of)'), ('GE', 'Georgia'), ('JP', 'Japan'), ('KG', 'Kyrgyzstan'), ('US', 'United States of America'), ('MM', 'Myanmar'), ('GS', 'South Georgia and the South Sandwich Islands'), ('CW', 'Curaçao'), ('KW', 'Kuwait'), ('OM', 'Oman'), ('JE', 'Jersey'), ('AF', 'Afghanistan'), ('LU', 'Luxembourg'), ('CR', 'Costa Rica'), ('CO', 'Colombia'), ('IO', 'British Indian Ocean Territory'), ('TO', 'Tonga'), ('FJ', 'Fiji'), ('PG', 'Papua New Guinea'), ('CY', 'Cyprus'), ('AS', 'American Samoa'), ('MG', 'Madagascar'), ('MO', 'Macao'), ('MP', 'Northern Mariana Islands'), ('PS', 'Palestine, State of'), ('NL', 'Netherlands'), ('IT', 'Italy'), ('ME', 'Montenegro'), ('IQ', 'Iraq'), ('KY', 'Cayman Islands'), ('KZ', 'Kazakhstan'), ('DK', 'Denmark'), ('BV', 'Bouvet Island'), ('TV', 'Tuvalu'), ('UA', 'Ukraine'), ('AD', 'Andorra'), ('TG', 'Togo'), ('ZM', 'Zambia'), ('ET', 'Ethiopia'), ('SD', 'Sudan'), ('JM', 'Jamaica'), ('GI', 'Gibraltar'), ('BS', 'Bahamas'), ('HM', 'Heard Island and McDonald Islands'), ('PW', 'Palau'), ('DE', 'Germany'), ('SC', 'Seychelles'), ('KE', 'Kenya'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('CH', 'Switzerland'), ('AE', 'United Arab Emirates'), ('IE', 'Ireland')], default='', max_length=2),
        ),
    ]
